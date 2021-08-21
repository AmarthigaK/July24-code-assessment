from django.db.models import fields
from rest_framework import serializers
from faculty.models import faculty

class facSerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty
        fields = ('code', 'facultyname','dept', 'add', 'mobile','username','password')