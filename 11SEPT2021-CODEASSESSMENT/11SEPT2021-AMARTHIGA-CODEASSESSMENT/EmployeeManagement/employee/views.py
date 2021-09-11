from django.shortcuts import render, redirect
from employee.models import Employee
from employee.serializer import empSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
import requests

# Create your views here.

#.....................Employee Registration..................#
@csrf_exempt
def collectemp(request):
    if(request.method == 'POST'):
        emp_serializer = empSerializer(data= request.POST)

        if(emp_serializer.is_valid()):
            emp_serializer.save()
            return redirect(login)

        else:
            return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to Employee Management System!")

@csrf_exempt
def viewuser(request, id):
    try:
        emp = Employee.objects.get(id= id)
        if(request.method == 'GET'):
            emp_serialize = empSerializer(emp)
            return JsonResponse( emp_serialize.data, safe = False, status = status.HTTP_200_OK)

        if(request.method == 'DELETE'):
            emp.delete()
            return HttpResponse("The details has been removed", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            empdata = JSONParser().parse(request)
            emp_serialize = empSerializer(emp, data= empdata)
            if(emp_serialize.is_valid()):
                emp_serialize.save()
                return JsonResponse(emp_serialize.data, status = status.HTTP_200_OK )

    except:
        return HttpResponse("Invalid data", status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def updateemp(request):
    try:
        getpass = request.POST.get("password")
        getupdate = Employee.objects.filter(password = getpass)
        emp_serialize = empSerializer(getupdate, many=True)
        return render(request, "empupdate.html", {"data":emp_serialize.data})

    except:
        return HttpResponse("Invalid data")

@csrf_exempt
def empupdateaction(request):
    getnewid = request.POST.get("Newid")
    getnewcode = request.POST.get("Newcode")
    getnewName = request.POST.get("Newname")
    getnewAdd = request.POST.get("Newaddress")
    getnewpin = request.POST.get("Newpin")
    getnewmob = request.POST.get("Newmob")
    getnewsalary = request.POST.get("Newsalary")
    getnewuser = request.POST.get("Newuser")
    getnewpassword = request.POST.get("Newpassword")
    empdata = {"id":getnewid, "empcode":getnewcode,"empname":getnewName,"address":getnewAdd,"pincode":getnewpin,"mobile":getnewmob, "salary":getnewsalary, "username":getnewuser, "password":getnewpassword}
    jsondata = json.dumps(empdata)

    apilink = "http://127.0.0.1:8000/employee/viewemp/"+getnewid
    requests.put(apilink, data=jsondata)
    return HttpResponse("Employee detail has been updated")







#Session
@csrf_exempt
def logincheck(request):
    try:
        getUser = request.POST.get("username")
        getpassword = request.POST.get("password")

        getuser = Employee.objects.filter(username=getUser, password= getpassword)
        user_serializer = empSerializer(getuser, many=True)
        print(user_serializer.data)
        if (user_serializer.data):
            for i in user_serializer.data:
                getID = i["id"]
                getCode = i["empcode"]
                # getName = i["empname"]
                # getAddress = i["address"]
                # getPin = i["pincode"]
                # getMob = i["mobile"]
                # getSal = i["salary"]
                getUser = i["username"]

            request.session['uid']=getID
            request.session['ucode']=getCode
            # request.session['uname']=getName
            # request.session['uadd']=getAddress
            # request.session['upin']=getPin
            # request.session['umob']=getMob
            # request.session['uuser']=getUSER
            # data = {"empcode":getCode,"empname":getName,"address":getAddress,"pincode":getPin,"mobile":getMob, "salary":getSal, "username":getUSER}
            return redirect(dashboard)
            return redirect(request, 'empdashboard.html', {"data":data})
    
        else:
            return HttpResponse("Invalid Credientials", status=status.HTTP_404_NOT_FOUND)

    except Employee.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")

def dashboard(request):
    try:
        getUid = request.session['uid']
        getusers = Employee.objects.get(id=getUid)
        emp_serialiser = empSerializer(getusers)  

        return render(request, 'empdashboard.html', {"data":emp_serialiser.data})

    except:
        return HttpResponse("Something went wrong, try again!")




#HTML

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "empsignup.html")

def login(request):
    return render(request, "emplogin.html")

def empupdate(request):
    return render(request, "empupdate.html")

def empprofile(request):
    return render(request, "profile.html")