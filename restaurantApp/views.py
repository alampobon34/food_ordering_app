from django.shortcuts import render
from restaurantApp.models import *

# Create your views here.


def all_restaurants(request):
    restaurants = Restaurant.objects.all()
    r = Restaurant.objects.get(id=3)
    print(r.id)
    cat = r.category.all()
    print(cat)
    context = {
        'restaurants':restaurants,
        'cat':cat,
    }
    return render(request,'all-restaurants.html',context) 



def restaurant_menu(request,id):
    restaurant = Restaurant.objects.get(id=id)

    category = restaurant.category.all()



    context = {
        'restaurant':restaurant,
        'category':category,
    }
    return render(request,'restaurant-menu.html',context)
