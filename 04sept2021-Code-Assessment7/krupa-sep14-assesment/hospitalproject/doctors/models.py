from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctorcode=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    special=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)
    username=models.CharField(max_length=40,default='',blank=True)
    password = models.CharField(max_length=40, default='', blank=True)
    # fname=models.CharField(max_length=40,default='',blank=True)



   