from django.contrib import admin
from .models import Menu, Dish, Order, Message

# Register your models here.

admin.site.register(Dish)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Message)
