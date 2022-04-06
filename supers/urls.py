from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_supers), 
    path('<int:pk>/', views.retrieve_super), 
]