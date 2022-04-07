from django.urls import path
from . import views


urlpatterns=[
    path('', views.list_super_types),
    path('<int:pk>/',views.super_type_details),
]