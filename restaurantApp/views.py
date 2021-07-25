from django.shortcuts import render
from restaurantApp.models import *

# Create your views here.


def all_restaurants(request):

    return render(request,'all-restaurants.html') 



def restaurant_menu(request,id):
    restaurant = Restaurant.objects.get(id=id)
    category = Category.objects.filter(restaurant_id=id)
    item = FoodItem.objects.all()


    context = {
        'category':category,
        'restaurant':restaurant,
        'item':item
    }
    return render(request,'restaurant-menu.html',context)
