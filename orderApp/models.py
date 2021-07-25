from django.db import models
from django.contrib.auth.models import User
from accountApp.models import *
from restaurantApp.models import *

# Create your models here.

STATUS_CHOICE = (
    ('Pending', 'Pending'),
    ('Cancel', 'Cancel'),
    ('Preparing', 'Preparing'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	status = models.CharField(default='Pending',choices=STATUS_CHOICE,max_length=20)
	transaction_id = models.CharField(max_length=100, null=True,blank=True)

	def __str__(self):
		return str(self.id) + ' ' + self.customer.user.username
		
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


class OrderItem(models.Model):
	product = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	def __str__(self):
		return "ID: " + str(self.order.id) + ' ' + self.product.name

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	area = models.CharField(max_length=200, null=False)
	houseNo = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address