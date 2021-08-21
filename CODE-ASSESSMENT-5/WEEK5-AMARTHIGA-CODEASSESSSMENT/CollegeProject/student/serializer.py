from django.db.models import fields
from rest_framework import serializers
from student.models import students

class stdSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('name', 'admno','rollno', 'college', 'parentname')



