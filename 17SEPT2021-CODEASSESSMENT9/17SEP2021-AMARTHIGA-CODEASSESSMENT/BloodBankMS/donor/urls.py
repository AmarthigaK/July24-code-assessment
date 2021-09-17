from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 

from donor import views

urlpatterns = [
    path('adddonor/', views.adddonor, name="adddonor"),
    path('loginuser/', views.loginuser, name="loginuser"),
    path('donordash/', views.donordash, name="donordash"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
]









#Django Admin Panel customization
admin.site.site_header = "Blood Bank Admin"
admin.site.site_title = " Welcome to Blood Bank Management System"
admin.site.index_title = " Welcome to Blood Bank Admin Portal"