from django.test import TestCase
from restaurantApp.models import *
from restaurantApp.views import *
from django.urls import reverse, resolve
#TestingModel
class RestaurantTest(TestCase):

    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(
            name = "Street Oven",
            address = "dhaka",
            description = "pasta pizza"
        )
    def test_restaurant(self):
        print(self.restaurant1.name)
        self.assertEqual(self.restaurant1.name,"Street Oven")

class CategoryTest(TestCase):
    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(
            name = "Street Oven",
            address = "dhaka",
            description = "pasta pizza"
        )
        self.category1 = Category.objects.create(
            restaurant = self.restaurant1,
            name = "Chicken"
        )
    def test_category(self):
        self.assertEqual(self.category1.name,"Chicken")

class FoodItemTest(TestCase):
    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(
            name = "Street Oven",
            address = "dhaka",
            description = "pasta pizza"
        )
        self.category1 = Category.objects.create(
            restaurant = self.restaurant1,
            name = "Chicken"
        )
        self.fooditem1 = FoodItem.objects.create(
            category = self.category1,
            name = "pasta",
            price = 525.52
        )
    def test_fooditem(self):
        self.assertEqual(self.fooditem1.name,"pasta")

#TestingURLS


class TestUrls(TestCase):

    def test_all_restaurantsUrl(self):
        urls = reverse('all-restaurants')
        self.assertEquals(resolve(urls).func, all_restaurants)

    def test_restaurants_menu(self):
        urls = reverse('restaurant-menu', args=[1])
        self.assertEquals(resolve(urls).func, restaurant_menu)