
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_supers), 
    path('<int:pk>/',views.list_heroes) #views.list_supers place holder
]