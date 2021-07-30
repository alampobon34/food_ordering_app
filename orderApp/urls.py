from typing import ChainMap
from django.urls import path
from orderApp.views import *




urlpatterns = [
    path('update_item/',updateItem,name='update_item'),
    path('cart/',cart,name='cart'),
    path('checkout/',check,name='checkout'),
    

]
