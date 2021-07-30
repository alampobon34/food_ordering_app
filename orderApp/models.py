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
	shipping_charge = models.DecimalField(max_length=100,decimal_places=2,max_digits=5,null=True,blank=True,default=50.00)
	is_complete = models.BooleanField(default=False)

	def __str__(self):
		return 'UserName: ' + self.customer.user.username
		
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

	@property
	def grand_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		if total >0:
			total +=self.shipping_charge
		else:
			self.shipping_charge = 0.00
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
		return self.product.name
	
	@property
	def get_category(self):
		return self.product.category

	@property
	def get_restaurant(self):
		return self.product.category.restaurant

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