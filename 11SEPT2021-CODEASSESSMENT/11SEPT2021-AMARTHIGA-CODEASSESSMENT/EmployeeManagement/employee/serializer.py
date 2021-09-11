from employee.models import Employee
from rest_framework import serializers
from django.db.models import fields


class empSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id","empcode","empname","address", "pincode", "mobile", "salary", "username","password")



        