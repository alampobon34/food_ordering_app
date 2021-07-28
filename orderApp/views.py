from django.shortcuts import render
from .models import *
from restaurantApp.models import *
from django.http import JsonResponse
import json
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer,status='Pending')
        items = order.orderitem_set.all()
        cartItems = order.orderitem_set.all()
        print(items)
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
        cartItems = order['get_cart_item']
    
    context ={
        'items' : items,
        'order': order,
        'cartItems':cartItems
    }
    return render(request, 'addtocart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']
    print(item_id)

    customer = request.user.profile
    fooditem = FoodItem.objects.get(id=item_id)
    order, created = Order.objects.get_or_create(customer=customer,status='Pending')
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=fooditem)
    if action =='add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse("item was added",safe=False)