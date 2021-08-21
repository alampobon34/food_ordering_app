from accountApp import urls
from django.test import SimpleTestCase
from django.test import TestCase, Client
from accountApp.models import *
from accountApp.views import *
from django.urls import reverse, resolve
import json

#Testing Model

class UserTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
        email = "kashfia@gmail.com",
        username = "kashfia@gmail.com",
        first_name = "Kashfia",
        last_name = "Saif",
        )
    def test_user(self):
        self.assertEqual(self.user1.email,"kashfia@gmail.com")

class AddressTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
        email = "kashfia@gmail.com",
        username = "kashfia@gmail.com",
        first_name = "Kashfia",
        last_name = "Saif",
        )
        self.address1 = Address.objects.create(
            user = self.user1,
            address_type = "home",
            address = "dhaka",
            area = "banasree",
            houseNo = "21",
            roadNo = "2",
            zipCode = "1217"
        )
    def test_address(self):
        self.assertEqual(self.address1.user.email,"kashfia@gmail.com")

class ProfileTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
        email = "kashfia@gmail.com",
        username = "kashfia@gmail.com",
        first_name = "Kashfia",
        last_name = "Saif",
        )
        self.profile1 = Profile.objects.create(
            user = self.user1,
            gender = "female",
            phone = "0197777777"
        )
    def test_profile(self):
        self.assertEqual(self.profile1.user.email,"kashfia@gmail.com")   

#TestingUrls
class TestUrls(TestCase):
    def test_homeUrl(self):
        urls = reverse('home')
        self.assertEquals(resolve(urls).func, index)

    def test_loginUrl(self):
        urls = reverse('login')
        self.assertEquals(resolve(urls).func, login_page)

    def test_addressUrl(self):
        urls = reverse('address')
        self.assertEquals(resolve(urls).func, address)

