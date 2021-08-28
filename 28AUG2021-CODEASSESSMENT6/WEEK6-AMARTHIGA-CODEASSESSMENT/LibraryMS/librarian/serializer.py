from django.db.models import fields
from rest_framework import serializers
from librarian.models import Lib

class libSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lib
        fields = ("id", "lib_code", "lname", "add", "mob", "pincode","email")