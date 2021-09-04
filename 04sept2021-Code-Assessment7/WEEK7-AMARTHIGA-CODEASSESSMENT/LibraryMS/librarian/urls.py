from django.urls import path, include
from librarian import views

urlpatterns = [ 
    #Back-end CRUD 
    path("Ladd/", views.addlib, name= "addlib"),
    path("Lviewall/", views.Lviewall, name= "Lviewall"),
    path("Lviewone/<id>", views.Lviewone, name= "Lviewone"),

    #Front-End CRUD
    path('entryl/', views.collect, name='collect'),
    path('searchl/', views.search, name='search'),
    path('updatel/', views.update, name='update'),
    path('updateact/', views.updateaction, name='updateaction'),
    path('deletel/', views.delete, name='delete'),
    path('deleteact/', views.delaction, name='delaction'),
    

    #HTML Pages
    path('', views.home, name='home'),
    path('entry/', views.entry, name='entry'),
    path('showall/', views.showallpage, name='showallpage'),
    path('search/', views.search, name='searchbook'),
    path('update/', views.update, name='updatebook'),
    path('delete/', views.dele, name='delbook'),


    #Session
    path('adduser/', views.adduser, name='adduser'),
    path('check_login/', views.check_login , name='check_login'),
    path('login/', views.login, name='login'),
    path('Lhome/', views.libhome, name='libhome'),

]