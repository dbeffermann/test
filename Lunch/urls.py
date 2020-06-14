from django.contrib import admin
from django.urls import path, include, reverse
from my_app.views import MenuListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('my_app.urls')),
    
 

]
