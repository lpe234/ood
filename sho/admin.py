# -*- coding: utf-8 -*-

from django.contrib import admin
from sho.models import User, Seller, Food, Order

__author__ = 'lpe234'
__date__ = '2014-11-22'

"""
设置admin，列表显示字段
"""


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'last_login_time', 'create_time']


class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'telephone', 'address', 'info', 'create_time']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'seller', 'create_time']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'food', 'info', 'create_time']

admin.site.register(User, UserAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin )