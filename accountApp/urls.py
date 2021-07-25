from typing import ChainMap
from django.urls import path
from accountApp.views import *



urlpatterns = [
    path('',index,name='home'),
    path('login/',login_page,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout_user,name='logout'),
    path('profile/',userProfile,name='userProfile'),
    path('orders/',orders,name='orders'),
    path('address/',address,name='address'),
    path('changepassword/',change_password,name='change_password'),
    path('buynow/',buy_now,name='buynow'),
    path('checkout/',checkout,name='checkout'),
    path('detail/',details,name='detail'),
    path('mobile/',mobile,name='mobile'),
    path('cp/',cp,name='cp'),
    path('address-update/',address_update,name="address-update"),
    #path('pills/',pills,name='pills'),
]
