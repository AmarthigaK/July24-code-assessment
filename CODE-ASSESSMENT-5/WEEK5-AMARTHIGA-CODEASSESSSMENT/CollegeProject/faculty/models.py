from django.db import models

# Create your models here.
class faculty(models.Model):
    code=models.IntegerField(default='')
    facultyname=models.CharField(max_length=50, default ='')
    dept = models.CharField(max_length=50, default ='')
    add=models.CharField(max_length=50, default ='')
    mobile=models.BigIntegerField(default='')
    username=models.CharField(max_length=50, default ='')
    password =models.CharField(max_length=50, default='') 
