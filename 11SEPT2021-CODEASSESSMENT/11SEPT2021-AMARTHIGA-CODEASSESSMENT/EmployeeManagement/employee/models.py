from django.db import models

# Create your models here.
class Employee(models.Model):
    empcode = models.CharField(max_length=50, default='')
    empname = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    pincode = models.CharField(max_length=50, default='')
    mobile = models.CharField(max_length=10,default='')
    salary = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    