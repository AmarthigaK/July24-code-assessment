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
    path('entry/', views.entry, name='bookentry'),
    path('showall/', views.showallpage, name='showallpage'),
    path('search/', views.search, name='searchbook'),
    path('update/', views.update, name='updatebook'),
    path('delete/', views.dele, name='delbook'),

]