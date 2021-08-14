from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def addfaculty(request):
    if (request.method == 'POST'):
        getName = request.POST.get('Faculty_Name')
        getadd = request.POST.get('Address')
        getdept = request.POST.get('Department')
        getcollege = request.POST.get('College')
        faculty_dic ={'Faculty_Name':getName, 'Address':getadd, 'Department':getdept, 'College':getcollege, };
        final =json.dumps(faculty_dic)
        return HttpResponse(final)

    else:
        return HttpResponse("HI, WELCOME!")