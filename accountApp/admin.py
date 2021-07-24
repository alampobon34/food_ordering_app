from django.contrib import admin
from accountApp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','username','is_admin','is_staff','is_active']
    list_filter = ['email', 'username']
    search_fields = ['email','username']

admin.site.register(User,UserAdmin)
admin.site.register(Profile)
admin.site.register(Address)