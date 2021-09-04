from django.urls import path, include
from books import views


urlpatterns = [ 
    #back-end CRUD
    path('add/', views.add, name='add'),
    path('viewall/', views.viewall, name='viewall'),
    path('viewone/<id>', views.viewone, name='viewone'),

    #Front-end CRUD
    path('entryb/', views.collect, name='collect'),
    path('searchb/', views.search, name='search'),
    path('updateb/', views.update, name='update'),
    path('updateact/', views.updateaction, name='updateaction'),
    path('deleteb/', views.delete, name='delete'),
    path('deleteact/', views.delaction, name='delaction'),
    

    #HTML Pages
    path('', views.home, name='home'),
    path('entry/', views.bookentry, name='bookentry'),
    path('showall/', views.showallpage, name='showallpage'),
    path('search/', views.searchbook, name='searchbook'),
    path('update/', views.updatebook, name='updatebook'),
    path('delete/', views.delbook, name='delbook'),
]