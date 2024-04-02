from django.shortcuts import render
from django.views import generic
from .models import Item        #from models.py


class MenuList(generic.ListView):   #this function requires very name specific variable
    queryset = Item.objects.order_by('date_created')
    template_name = 'index.html'

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'