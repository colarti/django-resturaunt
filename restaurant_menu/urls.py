from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),    #when the visitor the homes page, then get all information from index.html3=
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item')
]