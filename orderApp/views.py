from django.shortcuts import render
from .models import *
from restaurantApp.models import *
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer,status='Pending')
        items = order.orderitem_set.all()
        print(items)
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
    
    context ={
        'items' : items,
        'order': order,
    }
    return render(request, 'addtocart.html', context)