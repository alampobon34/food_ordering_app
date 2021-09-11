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
    reviews = Review.objects.filter(restaurant=restaurant)
    print(reviews)
    result = 0.00
    for rev in reviews:
        result += rev.rate / len(reviews)

    result = round(result, 2)


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
        'result':result,
    }
    return render(request,'restaurant-menu.html',context)



def item_search(request):

    cartItems=0
    query = request.GET['query']
    restaurant = Restaurant.objects.all()
    category = Category.objects.all()
    results = FoodItem.objects.filter(name__icontains=query)

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
    context={'results':results,
            'restaurant':restaurant,
            'category':category,
            'cartObjects':cartObjects,
            }
    return render(request,"item-search.html",context)
