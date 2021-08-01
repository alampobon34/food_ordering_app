from accountApp.forms import AddressUpdateForm
from django.shortcuts import render,redirect
from .models import *
from restaurantApp.models import *
from orderApp.forms import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order = Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            grand_total = order.grand_total
            cartObjects = orderItems.count()
        except:
            print('cart is empty..')
            cartObjects = 0
            grand_total=0
            order = {'get_cart_total': 0, 'get_cart_item': 0}
            orderItems=[]
            #cartItems = order['get_cart_item']
    else:
        cartObjects = 0
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        grand_total = 0
        orderItems=[]

    context = {
        'orderItems': orderItems,
        'order': order,
        'cartObjects': cartObjects,
        'grand_total':grand_total,
    }
    return render(request, 'addtocart.html', context)


@csrf_exempt
@login_required(login_url="login")
def updateItem(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']
    customer = request.user.profile
    fooditem = FoodItem.objects.get(id=item_id)
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=fooditem)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    if action == 'delete':
        orderItem.quantity = 0
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added", safe=False)




def checkout(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order = Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            grand_total = order.grand_total
            cartObjects = orderItems.count()
        except:
            print('cart is empty..')
            cartObjects = 0
            grand_total=0
            order = {'get_cart_total': 0, 'get_cart_item': 0}
            orderItems=[]
            #cartItems = order['get_cart_item']
    else:
        cartObjects = 0
        grand_total=0
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        orderItems=[]
        #cartItems = order['get_cart_item']

    if request.method=="POST":
        address = request.POST["address"]
        area = request.POST["area"]
        houseNo = request.POST["houseNo"]
        zipcode = request.POST["zipcode"]

        customer = request.user.profile
        order = Order.objects.get(customer=customer,is_complete=False)
        orderItems = OrderItem.objects.filter(order=order)
        order.is_complete=True
        order.save()
        address= ShippingAddress.objects.create(customer=customer,order=order,address=address,area=area,houseNo=houseNo,zipcode=zipcode)
        address.save()
        return redirect('checkout')

    context={
        'order':order,
        'grand_total':grand_total,
        'orderItems':orderItems,
        'cartObjects':cartObjects,
    }
    return render(request,'checkout.html',context)




def check(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.profile
            order = Order.objects.get(customer=customer,is_complete=False)
            orderItems = OrderItem.objects.filter(order=order)
            grand_total = order.grand_total
            cartObjects = orderItems.count()
        except:
            print('cart is empty..')
            cartObjects = 0
            grand_total=0
            order = {'get_cart_total': 0, 'get_cart_item': 0}
            orderItems=[]
            #cartItems = order['get_cart_item']
    else:
        cartObjects = 0
        grand_total=0
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        orderItems=[]
        #cartItems = order['get_cart_item']


    if request.method=="POST":
        try:
            customer = request.user.profile
            order = Order.objects.get(customer=customer,is_complete=False)
            address = request.POST["address"]
            area = request.POST["area"]
            houseNo = request.POST["houseNo"]
            zipcode = request.POST["zipcode"]

            address = ShippingAddress.objects.create(customer=customer,order=order,address=address,area=area,houseNo=houseNo,zipcode=zipcode)
            address.save()
            order.is_complete=True
            order.save()
            return redirect('home')
        except:
            pass

    
    context ={
        'order':order,
        'orderItems':orderItems,
        'grand_total':grand_total,
        'cartObjects':cartObjects,
    }
    return render(request,'checkout.html',context)