from django.shortcuts import render,redirect
from restaurantApp.models import *
from orderApp.models import *
# Create your views here.


def all_restaurants(request):

    return render(request,'all-restaurants.html') 



def restaurant_menu(request,id):
    cartItems=0
    category = Category.objects.filter(restaurant_id=id)
    restaurant = Restaurant.objects.get(id=id)
    item = FoodItem.objects.all()
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
        'category':category,
        'restaurant':restaurant,
        'cartObjects':cartObjects,
    }
    return render(request,'restaurant-menu.html',context)
