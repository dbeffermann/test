from django.contrib import admin
from django.urls import path, include, reverse
from my_app.views import MenuListView

#app_name = ""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls'),name="main"),

]
