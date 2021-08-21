from django.urls import path, include
from student import views


urlpatterns = [
    path('add/', views.addstd, name='addstd'),
    path('viewall/', views.viewstd, name='viewatd'),
    path('view/<id>', views.view, name='view'),
    path('admno/<fetchid>', views.adminno_view, name = 'adminno_view'),
    path('', views.reg, name='reg'),

]
