from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
import requests

from librarian.models import Lib
from librarian.serializer import libSerializer

# Create your views here.


#Basic CRUD Operations

@csrf_exempt
def addlib(request):
    if(request.method == 'POST'):
        libdata = JSONParser().parse(request)
        lib_serializer = libSerializer(data= libdata)

        if(lib_serializer.is_valid()):
            lib_serializer.save()
            return JsonResponse(lib_serializer.data, status = status.HTTP_200_OK)
            
        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to Add Librarian Page!")


@csrf_exempt
def Lviewall(request):
    if(request.method == 'GET'):
        lib=Lib.objects.all()
        lib_serializer = libSerializer(lib, many=True)
        return JsonResponse(lib_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view all Librarian details!")


@csrf_exempt
def Lviewone(request, id):
    try:
        lib = Lib.objects.get(id= id)
        if(request.method == 'GET'):
            lib_serialize = libSerializer(lib)
            return JsonResponse( lib_serialize.data, safe = False, status = status.HTTP_200_OK)

        if(request.method == 'DELETE'):
            lib.delete()
            return HttpResponse("The Librarian details has been removed", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            libdata = JSONParser().parse(request)
            lib_serialize = libSerializer(lib, data= libdata)
            if(lib_serialize.is_valid()):
                lib_serialize.save()
                return JsonResponse(lib_serialize.data, status = status.HTTP_200_OK )

    except:
        return HttpResponse("Invalid data", status = status.HTTP_400_BAD_REQUEST)


#Front-End CRUD
@csrf_exempt
def collect(request):
    if(request.method == 'POST'):
       lib_serializer = libSerializer(data= request.POST)
       if(lib_serializer.is_valid()):
            lib_serializer.save()
            return redirect(showallpage)
       else:
           return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to Library Management System!")

@csrf_exempt
def search(request):
    try:
        getcode = request.POST.get("lib_code")
        getSearch = Lib.objects.filter(lib_code=getcode)
        lib_serialize = libSerializer(getSearch, many=True)
        return render(request, 'searchL.html', {"data":lib_serialize.data})

    except:
        return HttpResponse("Invalid")

@csrf_exempt
def update(request):
    try:
        getcode = request.POST.get("lib_code")
        getupdate = Lib.objects.filter(lib_code = getcode)
        l_serialize = libSerializer(getupdate, many=True)
        return render(request, "updatelib.html", {"data":l_serialize.data})

    except:
        return HttpResponse("Invalid data")

@csrf_exempt
def updateaction(request):
    getnewid = request.POST.get("Newid")
    getnewCode = request.POST.get("Newcode")
    getnewname = request.POST.get("Newname")
    getnewadd = request.POST.get("Newadd")
    getnewmob = request.POST.get("Newmob")
    getnewpin = request.POST.get("Newpin")
    getnewemail = request.POST.get("Newemail")
    libdata = {"id":getnewid, "lib_code":getnewCode, "lname":getnewname, "add":getnewadd, "mob":getnewmob, "pincode":getnewpin,"email":getnewemail}
    jsondata = json.dumps(libdata)

    apilink = "http://127.0.0.1:8000/lib/Lviewone/"+getnewid
    requests.put(apilink, data=jsondata)
    return HttpResponse("Librarian detail has been updated")

@csrf_exempt
def delete(request):
    try:
        getcode = request.POST.get("lib_code")
        getdel = Lib.objects.filter(lib_code = getcode)
        l_serialize = libSerializer(getdel, many=True)
        return render(request, 'deletelib.html', {"data":l_serialize.data})
    except Lib.DoesNotExist:
        return HttpResponse("Invalid", status = status.HTTP_400_BAD_REQUEST)

    except:
        return HttpResponse("Somethimg went wrong!")

@csrf_exempt
def delaction(request):
    getnewid = request.POST.get("Newid")
    getnewCode = request.POST.get("Newcode")
    getnewname = request.POST.get("Newname")
    getnewadd = request.POST.get("Newadd")
    getnewmob = request.POST.get("Newmob")
    getnewpin = request.POST.get("Newpin")
    getnewemail = request.POST.get("Newemail")
    libdata = {"id":getnewid, "lib_code":getnewCode, "lname":getnewname, "add":getnewadd, "mob":getnewmob, "pincode":getnewpin,"email":getnewemail}
    jsondata = json.dumps(libdata)

    apilink = "http://127.0.0.1:8000/lib/Lviewone/"+getnewid
    requests.delete(apilink, data=jsondata)
    return HttpResponse("Librarian detail has been deleted")


#HTML Pages

def home(request):
    return render(request, 'home1.html')

def entry(request):
    return render(request, 'addlib.html')

def showallpage(request):
    getdata = requests.get("http://127.0.0.1:8000/lib/Lviewall/").json()
    return render(request, "showpageL.html", {"data":getdata})

def search(request):
    return render(request, 'searchL.html')

def update(request):
    return render(request, 'updatelib.html')

def dele(request):
    return render(request, 'deletelib.html')


#session
@csrf_exempt
def adduser(request):
    if (request.method == "POST"):
        try:
            getcode = request.POST.get("lib_code")
            getname = request.POST.get("lname")
            getadd = request.POST.get("add")
            getmob = request.POST.get("mob")
            getpin = request.POST.get("pincode")
            getemail = request.POST.get("email")
            getusername = request.POST.get("username")
            getpassword = request.POST.get("password")
            getuser = Lib.objects.filter(lib_code=getcode, lname=getname, add=getadd, mob=getmob, pincode=getpin, email=getemail, username = getusername, password= getpassword)
            user_serialiser = libSerializer(getuser, many=True)
            print(user_serialiser)
            if(user_serialiser):
                return HttpResponse("Already Exists data")

            else:
                user_serialiser = libSerializer(data = request.POST)
                if (user_serialiser.is_valid()):
                    user_serialiser.save()
                    return redirect(login)
                else:
                    return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

        except Lib.DoesNotExist:
            return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")

@csrf_exempt
def check_login(request):
    try:
        getUser = request.POST.get("username")
        getpassword = request.POST.get("password")

        getuser = Lib.objects.filter(username=getUser, password= getpassword)
        user_serializer = libSerializer(getuser, many=True)
        
        if (user_serializer.data):
            for i in user_serializer.data:
                getID = i["id"]
                getCode = i["lib_code"]
                getUser = i["username"]

            request.session['uid']=getID
            request.session['ucode']=getCode

            return redirect(libhome)
    
        else:
            return HttpResponse("Invalid")

    except Lib.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")


@csrf_exempt
def libhome(request):
    try:
        getUid = request.session['uid']
        getusers = Lib.objects.get(id=getUid)
        lib_serialiser = libSerializer(getusers)  

        return render(request, 'Libhome', {"data":lib_serialiser.data})

    except:
        return HttpResponse("Something went wrong, try again!")
        




        


def login(request):
    return render(request, "login.html")

