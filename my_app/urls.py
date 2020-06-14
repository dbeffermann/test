from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import TemplateView
from . import views

app_name="gview" #Nombre para accedes desde las urls del proyecto, "generic views integradas de Django"
urlpatterns = [
    path('', TemplateView.as_view(template_name='gview/main.html'),name='main'),
]

