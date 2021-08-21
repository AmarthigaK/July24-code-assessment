from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=50, default ='')
    admno = models.BigIntegerField(default='')
    rollno = models.BigIntegerField(default = '')
    college = models.CharField(max_length=50, default='')
    parentname = models.CharField(max_length=50, default='')

