from typing import ChainMap
from django.urls import path
from restaurantApp.views import *

urlpatterns = [
    path('all-restaurants/',all_restaurants,name='all-restaurants'),
    path('restaurant-menu/<int:id>/',restaurant_menu,name='restaurant-menu'),
    path('item-search/',item_search,name="item-search"),
]
