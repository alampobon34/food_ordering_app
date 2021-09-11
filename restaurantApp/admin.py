from django.contrib import admin
from restaurantApp.models import *
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','description']
    list_filter = ['address']


admin.site.register(Restaurant,RestaurantAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['get_restaurant', 'name']
    list_filter = ['name']
admin.site.register(Category,CategoryAdmin)



class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['get_restaurant', 'get_category','name','price']
    list_filter = ['name']

admin.site.register(FoodItem,FoodItemAdmin)




admin.site.register(Review)
