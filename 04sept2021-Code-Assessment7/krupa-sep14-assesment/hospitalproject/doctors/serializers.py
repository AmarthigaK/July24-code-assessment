from rest_framework import serializers
from doctors.models import Doctor

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('id','username','password','doctorcode','name','address','special','phone','email')