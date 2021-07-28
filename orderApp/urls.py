from typing import ChainMap
from django.urls import path
from orderApp.views import *




urlpatterns = [
    path('cart/',cart,name='cart'),
    path('update_item/',updateItem,name='update_item')

]
