from django.db import models

# Create your models here.


class Donor(models.Model):
    name=models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    bloodgroup = models.CharField(max_length=50, default='')
    mobile = models.CharField(max_length =50, default='')
    username = models.CharField(max_length =50, default='')
    password = models.CharField(max_length=50, default='')
    created = models.DateTimeField(auto_now_add=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)


    def __str__(self):
        return self.name + "-" +self.bloodgroup + "-" + self.mobile

