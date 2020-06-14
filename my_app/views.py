from django.shortcuts import render, get_object_or_404,redirect
from .models import Menu


def MenuListView(request):
    queryset = Menu.objects.all() #Listado de Menus creados
    context  = {
        "object_list": queryset
    }
    return render(request,"Menu/Menu_list.html", context)


