from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http.response import JsonResponse

from faculty.models import faculty
from faculty.serializer import facSerializer
# Create your views here.

@csrf_exempt
def addfac(request):
    if(request.method =='POST'):
        facdata = JSONParser().parse(request)
        fac_serialize = facSerializer(data=facdata)

        if(fac_serialize.is_valid()):
            fac_serialize.save()
            return JsonResponse(fac_serialize.data, status= status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization", status = status.HTTP_404_NOT_FOUND)

    else:
        return HttpResponse("Welcome to Add Faculty Details Page!")

@csrf_exempt
def viewfac(request):
    if(request.method == 'GET'):
        fac=faculty.objects.all()
        fac_serializer = facSerializer(fac, many=True)
        return JsonResponse(fac_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view all faculty details!")

@csrf_exempt
def view(request, id):
    try:
        fac = faculty.objects.get(id=id)
        if(request.method =='GET'):
            fac_serialize = facSerializer(fac)
            return JsonResponse(fac_serialize.data, safe = False, status = status.HTTP_200_OK )

        if(request.method == 'DELETE'):
            fac.delete()
            return HttpResponse("Student details has removed", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            facdata = JSONParser().parse(request)
            fac_serialize =facSerializer(fac, data=facdata)
            if(fac_serialize.is_valid()):
                fac_serialize.save()
                return JsonResponse(fac_serialize.data, status = status.HTTP_200_OK)
        
    except:
        return HttpResponse("Invalid data", status - status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def code_view(request, fetchid):
    try:
        facu = faculty.objects.get(code=fetchid)
        if(request.method == 'GET'):
            faculty_serialize = facSerializer(facu)
            return JsonResponse(faculty_serialize.data, safe=False, status=status.HTTP_200_OK)

        

    except faculty.DoesNotExist:
        return HttpResponse("Invalid Admission No", status=status.HTTP_400_BAD_REQUEST)


def regfac(request):
    return render (request, 'facadd.html')