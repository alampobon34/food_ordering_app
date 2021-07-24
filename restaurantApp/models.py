from django.db import models

# Create your models here.



class Menu(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(blank=True,null=True,upload_to='menu_img',default='order-img.jpg')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    Menu = models.ManyToManyField(Menu,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True,max_length=500)
    image = models.ImageField(blank=True,null=True,upload_to='restaurent_img',default='g-1.jpg')


    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True,max_length=500)
    price = models.DecimalField(null=True,blank=True,max_length=100,decimal_places=2,max_digits=5)
    image = models.ImageField(blank=True,null=True,upload_to='restaurent_img',default='g-1.jpg')


    def __str__(self):
        return self.name
