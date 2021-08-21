from django.test import TestCase
from restaurantApp.models import *
<<<<<<< HEAD

# Create your tests here.














































































































=======
from restaurantApp.views import *
from django.urls import reverse, resolve
#TestingModel
>>>>>>> origin/unittesting_restaurantapp
class RestaurantTest(TestCase):

    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(
            name = "Street Oven",
            address = "dhaka",
            description = "pasta pizza"
        )


    def test_restaurant(self):
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

<<<<<<< HEAD
class CategoryTest(TestCase):
    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(
            name = "Street Oven",
            address = "dhaka",
            description = "pasta pizza"
        )

        self.category1 = Category.objects.create(
            restaurant = self.restaurant1,
            name="Chicken")
    
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
            price= 300.00,
        )
    def test_fooditem(self):
        self.assertEqual(self.fooditem1.name,"pasta")

=======
    def test_all_restaurantsUrl(self):
        urls = reverse('all-restaurants')
        self.assertEquals(resolve(urls).func, all_restaurants)
>>>>>>> origin/unittesting_restaurantapp

    def test_restaurants_menu(self):
        urls = reverse('restaurant-menu', args=[1])
        self.assertEquals(resolve(urls).func, restaurant_menu)