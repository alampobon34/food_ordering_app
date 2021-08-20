from django.test import TestCase
from restaurantApp.models import *

# Create your tests here.


class TestModels(TestCase):

    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(
            name = "Street Oven",
            address = "dhaka",
            description = "pasta pizza"
        )
    def test_restaurant(self):
        print(self.restaurant1.name)
        self.assertEqual(self.restaurant1.name,"Street Oven")



