from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def addstd(request):
    if (request.method == 'POST'):
        getName = request.POST.get('Student_Name')
        getadmin = request.POST.get('AdmissionNo')
        getroll = request.POST.get('RollNo')
        getcollege = request.POST.get('College')
        getparent = request.POST.get('Parent_Name')
        student_dic ={'Student_Name':getName, 'AdmissionNo':getadmin, 'RollNo':getroll, 'College':getcollege, 'Parent_Name':getparent,};
        final =json.dumps(student_dic)
        return HttpResponse(final)

    else:
        return HttpResponse("HI, WELCOME!")
        