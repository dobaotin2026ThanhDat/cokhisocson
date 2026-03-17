from django.urls import path
from . import views

urlpatterns = [

path('', views.home),

path('nhan-bao-gia/', views.quote),
path('dich-vu/', views.services),

path('du-an/', views.projects),
path('ho-so-nang-luc/', views.profile),
]