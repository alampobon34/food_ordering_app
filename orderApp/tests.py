from django.test import TestCase, Client
from django.urls import reverse
from accountApp.models import *
import json
from orderApp.models import *
#from __future__ import unicode_literals
#from django.utils.encoding import force_text
from accountApp import models
from restaurantApp import models
from django.http import HttpRequest
#from django.contrib.auth.models import User

#from billing.forms import InvoiceForm

# Create your tests here.

class URLTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('admin', 'admin@gmail.com',  'admin123')
        self.client = Client()
        self.cart_url = reverse('cart')

    def testUrl_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "update_item url failed")

    def testUrl_cart(self):
        response_update_item = self.client.get('/cart/')
        self.assertEqual(response_update_item.status_code, 200, "cart url failed")

    def testUrl_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200, "checkout url failed")

    def testUrl_update_item(self):
        response = self.client.get('/update_item/')
        #self.assertJSONEqual(force_text(response.content), {'safe': False}, "checkout url failed")

class Views_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('samiunsizan', 'samiunsizan@gmail.com',  'admin@123')
        self.client = Client()
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')


    def testView_Cart(self):
        #client = Client()
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200, "Cart view failed")
        self.assertTemplateUsed(response,'addtocart.html',"Checking template of addtocart")

    #def testView_Cart_After_Add_Product(self):
        #client = Client()

    def testView_CheckOut(self):
        # client = Client()
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200, "Cheakout view failed")
        self.assertTemplateUsed(response, 'checkout.html',"Checking template of checkout")

class models_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('samiunsizan', 'samiunsizan@gmail.com',  'admin@123')
        self.client = Client()
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')
        self.User1 = User.objects.create(
            email = "samiunsizan1@gmail.com",
            username = "samiun1",
            first_name ="samiun",
            last_name = "sizan"
        )
        self.profile1 = Profile.objects.create(
            user = self.User1


        )
        self.order1 = Order.objects.create(
            customer = self.profile1,
            is_complete = False
        )

        self.restaurant1 = Restaurant.objects.create(
            name="Street Oven",
            address="dhaka",
            description="pasta pizza"
        )

        self.category1 = Category.objects.create(
            restaurant=self.restaurant1,
            name="Chicken")

        self.fooditem1 = FoodItem.objects.create(
            category=self.category1,
            name="pasta",
            price=300.00,
        )

        self.orderitem1 = OrderItem.objects.create(
            product = self.fooditem1,
            order = self.order1,
            quantity = 2
        )

        self.shippingaddress1 = ShippingAddress.objects.create(
            customer=self.profile1,
            order = self.order1,
            address = "Dhaka",
            area = "Badda",
            houseNo = "Road 14, House 20",
            zipcode = "1212"
        )

    def test_order(self):
        self.assertEqual(self.order1.is_complete,False,"Checking order completed or not")
        self.assertEqual(self.order1.customer.user.username,"samiun1","Testing unsername of the order")
        self.assertEqual(self.order1.get_cart_items, 2,"Testing Number of items")
        self.assertEqual(self.order1.get_cart_total, 600,"Testing Cart Total")

    def test_orderItem(self):
        self.assertEqual(self.orderitem1.quantity,2,"Testing quantity of the ordered item")
        self.assertEqual(self.orderitem1.product.category.restaurant.name,"Street Oven","Testing restaurent name of the ordered item")
        self.assertEqual(self.orderitem1.get_total,600,"Testing total ammount of the ordered item")
        self.assertEqual(self.orderitem1.get_category,self.category1,"Testing quantity of the ordered item")

    def test_shippingAddress(self):
        self.assertEqual(self.shippingaddress1.address,"Dhaka","testing address")













