from django.contrib import admin

from .models import Car,Customer
# Register your models here.

class Caradmin(admin.ModelAdmin):
    list_display=['cname','price','model','variant','color','engine']
    search_fields=['cname','engine']


class custadmin(admin.ModelAdmin):
    list_display=['name','mob','English','Kannada','Hindi','Telugu','Tamil']

admin.site.register(Car,Caradmin)
admin.site.register(Customer,custadmin)