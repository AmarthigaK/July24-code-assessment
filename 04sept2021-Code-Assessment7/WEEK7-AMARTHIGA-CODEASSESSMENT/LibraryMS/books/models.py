from django.db import models

# Create your models here.
class Books(models.Model):
    bname = models.CharField(max_length=50, default= '')
    author = models.CharField(max_length=50, default= '')
    descrip = models.CharField(max_length=50, default= '')
    price = models.IntegerField(default= '')
    category = models.CharField(max_length=50, default= '')