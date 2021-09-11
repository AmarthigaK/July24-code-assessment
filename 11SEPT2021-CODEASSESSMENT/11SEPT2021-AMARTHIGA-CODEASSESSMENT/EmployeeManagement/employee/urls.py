from django.urls import path, include
from employee import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('empsignup/', views.signup, name="signup"),
    path('emplogin/', views.login, name="login"),
    path('empupdate/', views.empupdate, name="empupdate"),
    path('empprofile/', views.empprofile, name="empprofile"),

    path('collectemp/', views.collectemp, name="collectemp"),
    path('viewemp/', views.viewuser, name="viewuser"),
    path('updateemp/', views.updateemp, name="updateemp"),
    path('updateactionemp/', views.empupdateaction, name="empupdateaction"),

    #path('addemp/', views.addemployee, name="addemployee"),
    path('check/', views.logincheck, name="logincheck"),
    path('dashboard/', views.dashboard, name="dashboard"),

]