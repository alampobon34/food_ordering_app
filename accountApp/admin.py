from django.contrib import admin
from accountApp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','username','is_admin','is_staff','is_active']
    list_filter = ['email', 'username']
    search_fields = ['email','username']

admin.site.register(User,UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender','phone','birthDate','image']
admin.site.register(Profile,ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'area','houseNo','roadNo','zipCode']

admin.site.register(Address,AddressAdmin)