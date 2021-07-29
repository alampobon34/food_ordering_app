from django.shortcuts import render
from .models import *
from restaurantApp.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(
            customer=customer, is_complete=False)
        items = order.orderitem_set.all()
        cartItems = order.orderitem_set.all()
        grand_total = order.grand_total

        print(items)
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'grand_total':grand_total,
    }
    return render(request, 'addtocart.html', context)


@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']
    customer = request.user.profile
    fooditem = FoodItem.objects.get(id=item_id)
    order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=fooditem)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    if action == 'delete':
        orderItem.quantity = 0
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("item was added", safe=False)


# def updateItem(request):
#     data = json.loads(request.body)
#     item_id = data['item_id']
#     quantity = data['quantity']
#     action = data['action']
#     print(item_id)

#     customer = request.user.profile
#     fooditem = FoodItem.objects.get(id=item_id)
#     order, created = Order.objects.get_or_create(customer=customer,status='Pending')
#     orderItem, created = OrderItem.objects.get_or_create(order=order,product=fooditem,quantity=quantity)
#     if action =='add':
#         orderItem.quantity = (orderItem.quantity +1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity -1)
#     elif action == 'delete':
#         orderItem.quantity=0
#     orderItem.save()
#     if orderItem.quantity <=0:
#         orderItem.delete()
#     return JsonResponse("item was added",safe=False)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order,created = Order.objects.get_or_create(customer=customer,is_complete=False)
        orderItems = order.orderitem_set.all()
        grand_total = order.grand_total

        context={
            'orderItems':orderItems,
            'grand_total':grand_total
        }
    return render(request,'checkout.html',context)