from django.shortcuts import render
from django.views import generic
from .models import Item        #from models.py
from .models import MEAL_TYPE


class MenuList(generic.ListView):   #this function requires very name specific variable
    queryset = Item.objects.order_by('date_created')
    template_name = 'index.html'

    def get_context_data(self, **kwargs): #this is specific named for django
        context = super().get_context_data(**kwargs)    #this will pull the data from the database
        context['meals'] = MEAL_TYPE

        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'