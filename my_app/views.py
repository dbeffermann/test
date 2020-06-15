from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Menu


#Lista Basada en funcion.
def MenuListView(request):
    queryset = Menu.objects.all() #Created Menus List. 
    context  = {
        "object_list": queryset
    }
    return render(request,"Menu/Menu_list.html", context)

def MenuDetailView(request,id): #Need to pass pk or other field of the model.
    obj = get_object_or_404 (Menu,id=id) #The result is One single register 
    context  = {
        "object_list": obj
    }
    return render(request,"Menu/Menu_detail.html", context)


#List Based on a Django's generic view class. (comment: next step is to reflect this on the actual template)
class Menu_list_view_generic(ListView):
     template_name = "Menu/Menu_list_generic.html"
     queryset = Menu.objects.all()

  

