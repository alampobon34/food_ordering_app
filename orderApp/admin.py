from django.contrib import admin
from .models import *
# Register your models here.





class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered','grand_total','get_cart_items','status','is_complete']
    search_fields = ['status','is_complete']

admin.site.register(Order,OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['get_restaurant','get_category','product', 'order','quantity']
    search_fields = ['order']


admin.site.register(OrderItem,OrderItemAdmin)


class ShippingAddressemAdmin(admin.ModelAdmin):
    list_display = ['customer','order','area', 'houseNo','zipcode']
    search_fields = ['order']

admin.site.register(ShippingAddress,ShippingAddressemAdmin)