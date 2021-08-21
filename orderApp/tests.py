from django.test import TestCase, Client
from django.urls import reverse
from accountApp.models import *
import json
from orderApp.models import *
#from __future__ import unicode_literals
#from django.utils.encoding import force_text

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
        self.assertTemplateUsed(response,'addtocart.html')

    #def testView_Cart_After_Add_Product(self):
        #client = Client()

    def testView_CheckOut(self):
        # client = Client()
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200, "Cheakout view failed")
        self.assertTemplateUsed(response, 'checkout.html')

class Views_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('admin1', 'admin@gmail.com',  'admin123')
        self.





