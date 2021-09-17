from django.shortcuts import render, redirect
from donor.models import *
from donor.serializer import *

from django.views.decorators.csrf import csrf_exempt
from django.http import request
import requests
from django.http.response import HttpResponse,JsonResponse
from rest_framework import status
import json

# Create your views here.

@csrf_exempt
def adddonor(request):
    if(request.method == 'POST'):
        try:
            getName = request.POST.get("name")
            getAdd = request.POST.get("address")
            getBldgrp = request.POST.get("bloodgroup")
            getmobile = request.POST.get("mobile")
            getuser = request.POST.get("username")
            getpassword = request.POST.get("password")

            donor_dic = {"name":getName, "address":getAdd, "bloodgroup":getBldgrp, "mobile":getmobile, "username":getuser, "password":getpassword}
            print(donor_dic)
            don = DonorSerializer(data = donor_dic)
            print(don)
            if don.is_valid():
                don.save()
                return JsonResponse(don.data, safe=False, status=status.HTTP_200_OK)

        except:
            return HttpResponse("Try again!")


@csrf_exempt
def loginuser(request):
    try:
        getuser = request.POST.get("username")
        getpass = request.POST.get("password")

        getDonor = Donor.objects.filter(username = getuser, password=getpass)
        donor_serilaizer =DonorSerializer(getDonor, many =True)
        print(donor_serilaizer)


        if (donor_serilaizer):
            for i in donor_serilaizer.data:
                getId = i["id"]
                getName = i["name"]
                getAdd = i["address"]
                getMob = i["mobile"]
                getbldgrp = i["bloodgroup"]
                getUser = i["username"]
                getpassword = i["password"]

            request.session['did']=getId
            request.session['dname']=getName
            request.session['dadd']=getAdd
            request.session['dmob']=getMob
            request.session['dbldgrp']=getbldgrp
            request.session['username']=getUser
            request.session['password']=getpassword

            return redirect(donordash)

        else:
            return HttpResponse("Invalid Credientials", status=status.HTTP_404_NOT_FOUND)

    except Donor.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")




def donordash(request):
    try:
        getDid = request.session['did']
        getcustomer = Donor.objects.get(id=getDid)
        cus_serialiser = DonorSerializer(getcustomer)

        return render(request, "donordashboard.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")


def home(request):
    return render(request, 'home.html')
    

def login(request):
    return render(request, 'donorlogin.html')

        





