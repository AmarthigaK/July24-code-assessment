from django.db import models

# Create your models here.
#librarian_code, name, address, mobile, pincode, emailid
class Lib(models.Model):
    lib_code = models.IntegerField(default= '')
    lname = models.CharField(max_length=50, default= '')
    add = models.CharField(max_length=50, default= '')
    mob = models.BigIntegerField(default= '')
    pincode = models.CharField(max_length=50, default= '')
    email = models.CharField(max_length=50, default= '')
    username = models.CharField(max_length=50, default = '')
    password = models.CharField(max_length=50, default = '')
    
    


