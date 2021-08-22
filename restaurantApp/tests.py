from django.test import TestCase, Client
from django.urls import reverse
from orderApp import views
from restaurantApp.models import *






# Create your tests here.
class view_Test(TestCase):
    def setUp(self):
        self.client= Client()
        self.restaurant_url = reverse('all-restaurants')
        self.restaurant_menu_url = reverse('restaurant-menu', args=[1])

    def TestView_allrestaurant(self):
        response = self.client.get(self.restaurant_url)
        self.assertEqual(response.status_code, 200, "restaurant view failed")
        self.assertTemplateUsed(response, 'all-restaurants.html', "Checking template of restaurant")

    def TestView_restaurantmenu(self):
        response = self.client.get(self.restaurant_menu_url)
        self.assertEqual(response.status_code, 200, "restaurant menu view failed")
        self.assertTemplateUsed(response, 'restaurant-menu.html', "Checking template of restaurant")

