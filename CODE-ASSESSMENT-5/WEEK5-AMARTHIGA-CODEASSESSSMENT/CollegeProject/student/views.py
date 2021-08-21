#For HTML user interface 
from django.shortcuts import render

#For CRUD operations
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http.response import JsonResponse

#Form student application importing models and serializers
from student.models import students
from student.serializer import stdSerializer

# Create your views here.

@csrf_exempt
def addstd(request):
    if(request.method =='POST'):
        stddata = JSONParser().parse(request)
        std_serialize = stdSerializer(data=stddata)

        if(std_serialize.is_valid()):
            std_serialize.save()
            return JsonResponse(std_serialize.data, status= status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization", status = status.HTTP_404_NOT_FOUND)

    else:
        return HttpResponse("Welcome to Add Student Details Page!")

@csrf_exempt
def viewstd(request):
    if(request.method == 'GET'):
        std=students.objects.all()
        std_serializer = stdSerializer(std, many=True)
        return JsonResponse(std_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view all student details!")

@csrf_exempt
def view(request, id):
    try:
        std = students.objects.get(id=id)
        if(request.method =='GET'):
            std_serialize = stdSerializer(std)
            return JsonResponse(std_serialize.data, safe = False, status = status.HTTP_200_OK )

        if(request.method == 'DELETE'):
            std.delete()
            return HttpResponse("Student details has removed", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            stddata = JSONParser().parse(request)
            std_serialize =stdSerializer(std, data=stddata)
            if(std_serialize.is_valid()):
                std_serialize.save()
                return JsonResponse(std_serialize.data, status = status.HTTP_200_OK)
        
    except:
        return HttpResponse("Invalid data", status - status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def adminno_view(request, fetchid):
    try:
        student = students.objects.get(admno=fetchid)
        if(request.method == 'GET'):
            student_serialize = stdSerializer(student)
            return JsonResponse(student_serialize.data, safe=False, status=status.HTTP_200_OK)

        if(request.method == 'DELETE'):
            student.delete()
            return HttpResponse("Student details has removed with Admission No", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            stddata = JSONParser().parse(request)
            student_serialize =stdSerializer(student, data=stddata)
            if(student_serialize.is_valid()):
                student_serialize.save()
                return JsonResponse(student_serialize.data, status = status.HTTP_200_OK)

    except students.DoesNotExist:
        return HttpResponse("Invalid Admission No", status=status.HTTP_400_BAD_REQUEST)


def reg(request):
    return render (request, 'stdadd.html')







    

