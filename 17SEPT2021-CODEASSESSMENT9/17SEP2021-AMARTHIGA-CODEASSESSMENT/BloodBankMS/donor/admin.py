from django.contrib import admin
from donor.models import *

# Register your models here.

class donorProfile(admin.ModelAdmin):
    fields = ("name", "address", "bloodgroup", "mobile", "username", "password", "id")


    search_fields = ("name", "bloodgroup", "mobile")

    list_filter = [
        "name",
        "bloodgroup",
        "mobile" 
    ]

admin.site.register(Donor, donorProfile)