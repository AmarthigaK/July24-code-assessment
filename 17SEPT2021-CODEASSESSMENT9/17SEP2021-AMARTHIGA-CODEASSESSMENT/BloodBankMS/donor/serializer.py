from rest_framework import serializers
from django.db.models import fields
from donor.models import Donor


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = {"name", "address", "bloodgroup", "mobile", "username", "password", "id" }