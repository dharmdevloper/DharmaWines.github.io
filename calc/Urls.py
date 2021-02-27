from django.contrib import admin
from django.urls import path
from calc import views


urlpatterns = [
    path('', views.login, name='calc'),
    path('index',views.index,name='index' ),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact')
]