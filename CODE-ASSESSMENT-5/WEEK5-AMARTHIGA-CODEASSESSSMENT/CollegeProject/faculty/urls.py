from django.urls import path, include
from faculty import views

urlpatterns=[ 
    path('add/', views.addfac, name='addfac'),
    path('viewall/', views.viewfac, name='viewfac'),
    path('view/<id>', views.view, name='view'),
    path('fcode/<fetchid>', views.code_view, name = 'code_view'),
    path('', views.regfac, name='regfac'),
]