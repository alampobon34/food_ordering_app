from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from accountApp.forms import *
from django.contrib import messages
from accountApp.models import *
from restaurantApp.models import *
from orderApp.models import *

# Create your views here.


def index(request):
    restaurants = Restaurant.objects.all()
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order= Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            cartObjects = orderItems.count()
        except:
            cartObjects = 0

    else:
        cartObjects = 0
    context = {
        'restaurants':restaurants,
        'cartObjects':cartObjects,

    }
    return render(request,'home.html',context) 


# def login_page(request):
#     message = None
#     if request.POST:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request,email=email, password=password)
#         print(email,password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html')
#     return render(request, 'login.html')



def login_page(request):
    cartObjects = 0
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:

                messages.error(request,'Invalid Email or Password....!!')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request,'Invalid Email or Password....!!')
            return render(request, 'login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': form,
        'cartObjects':cartObjects
    }
    return render(request, 'login.html', context)


def register(request):
    cartObjects = 0
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            profile = Profile.objects.create(user=user)
            address = Address.objects.create(user=user)
            login(request, user)
            return redirect('home')
        else:
            context ={'form':form}
            return render(request, 'customerregistration.html', context)
    form = UserRegistrationForm()
    context ={'form':form,'cartObjects':cartObjects}
    return render(request, 'customerregistration.html',context)



def logout_user(request):
    logout(request)
    messages.success(request,'Logout Successfully....!!')
    return redirect('login')




def profile(request):
    

    return render(request,'profile.html')


def orders(request):
    return render(request,'orders.html')

def address(request):
    return render(request,'address.html')



def change_password(request):
    return render(request,'changepassword.html')



def buy_now(request):
    return render(request,'buynow.html')





def details(request):
    return render(request,'productdetail.html')


def mobile(request):
    if request.method=="POST":
        a_form = AddressUpdateForm(request.POST,instance=request.user.address)
        if a_form.is_valid():
            a_form.save()
            return redirect('userProfile')
        else:
            a_form = AddressUpdateForm(request.POST,instance=request.user.address)
            context = {'a_form' : a_form}
            return render(request,'profile.html',context)

    a_form = AddressUpdateForm(instance=request.user.address)
    context = {'a_form' : a_form}
    return render(request, 'mobile.html',context)














@login_required(login_url="login")
def change_password(request):
    orderList = []
    
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order= Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            cartObjects = orderItems.count()
            orderList = Order.objects.filter(customer=customer)
            print(orderList)
        except:
            cartObjects = 0

    else:
        cartObjects = 0
    
    if request.method== "POST":

        form = PasswordChangingForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            email = request.user.email
            password = request.POST['new_password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = PasswordChangingForm(user=request.user,data=request.POST)
    else:
        form = PasswordChangingForm(user=request.user)
    context = {'form' : form,
                'cartObjects':cartObjects,'orderList':orderList}
    print(orderList)
    return render(request,'changepassword.html',context)












def cp(request):
    
    if request.method== "POST":
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PasswordChangeForm(user=request.user,data=request.POST)
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form' : form,

                }
    return render(request,'userProfile.html',context)



@login_required(login_url="login")
def userProfile(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order= Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            cartObjects = orderItems.count()
            
        except:
            cartObjects = 0

    else:
        cartObjects = 0

    pk = request.user.address.pk
    address = Address.objects.get(pk=pk)
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('userProfile')
        else:
            u_form = UserUpdateForm(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
            context = {'u_form' : u_form,
                        'p_form':p_form,
                        'orderItems':orderItems,
                        'grand_total':grand_total,
                        'cartItems':cartItems,
                        'orderList':orderList}
            return render(request, 'userProfile.html',context)
    else:
        orderList = Order.objects.filter(customer=customer)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'u_form' : u_form,'p_form':p_form,'address':address,
                    'cartObjects':cartObjects,
                    'orderList':orderList}

        print(orderList)
        return render(request, 'userProfile.html',context)


@login_required(login_url="login")
def address_update(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order= Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            cartObjects = orderItems.count()
        except:
            cartObjects = 0

    else:
        cartObjects = 0
    if request.method=="POST":
        a_form = AddressUpdateForm(request.POST,instance=request.user.address)
        if a_form.is_valid():
            a_form.save()
            return redirect('userProfile')
        else:
            a_form = AddressUpdateForm(request.POST,instance=request.user.address)
            context = {'a_form' : a_form,
                        'cartObjects':cartObjects,
            }
            return render(request,'addressUpdate.html',context)

    a_form = AddressUpdateForm(instance=request.user.address)
    context = {'a_form' : a_form,
            'cartObjects':cartObjects,}
    return render(request, 'addressUpdate.html',context)