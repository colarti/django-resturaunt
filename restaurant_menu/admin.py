from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')   #the variables are coming from models.py in class Item
    list_filter = ('status',)
    search_fields = ('meal', 'description')


admin.site.register(Item, MenuItemAdmin)    #register couples the models.Item with this MenuItemAdmin


