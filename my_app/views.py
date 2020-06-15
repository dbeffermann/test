from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Menu


#Lista Basada en funcion.
def MenuListView(request):
    queryset = Menu.objects.all() #Listado de Menus creados. 
    context  = {
        "object_list": queryset
    }
    return render(request,"Menu/Menu_list.html", context)


#List Based on a Django's generic view class. (comment: next step is to reflect this on the actual template)
class Menu_list_view_generic(ListView):
    #template_name = "Menu/Menu_list_generic.html"
    model = Menu
    queryset = Menu.objects.all()
    

