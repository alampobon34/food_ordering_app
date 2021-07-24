from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(blank=True,null=True,upload_to='Category-images/')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    category = models.ManyToManyField(Category,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True,max_length=500)
    image = models.ImageField(blank=True,null=True,upload_to='Restaurent-images')


    def __str__(self):
        return self.name


class FoodItem(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_length=100,decimal_places=2,max_digits=5)
    image = models.ImageField(blank=True,null=True,upload_to='FoodItem-images')

    def __str__(self):
        return self.name
