from typing import ChainMap
from django.urls import path
from accountApp.views import *



urlpatterns = [
    path('',index,name='home'),
    path('login/',login_page,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout_user,name='logout'),
    path('profile/',userProfile,name='userProfile'),
    path('order-delete/',delete_order,name="order_delete"),
    path('changepassword/',change_password,name='change_password'),

    path('address-update/',address_update,name="address-update"),
]
