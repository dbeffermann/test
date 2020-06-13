from django.contrib import admin
from .models import Menu, Plato, Orden, Mensaje

# Register your models here.

admin.site.register(Plato)
admin.site.register(Menu)
admin.site.register(Orden)
admin.site.register(Mensaje)
