from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
import requests

from books.models import Books
from books.serializer import bookSerializer

# Create your views here.

#Basic CRUD

@csrf_exempt
def add(request):
    if(request.method == 'POST'):
        bookdata = JSONParser().parse(request)
        bok_serializer = bookSerializer(data= bookdata)

        if(bok_serializer.is_valid()):
            bok_serializer.save()
            return JsonResponse(bok_serializer.data, status = status.HTTP_200_OK)
            
        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to Add Books Page!")

@csrf_exempt
def viewall(request):
    if(request.method == 'GET'):
        book=Books.objects.all()
        book_serializer = bookSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view all Book details!")

@csrf_exempt
def viewone(request, id):
    try:
        book = Books.objects.get(id= id)
        if(request.method == 'GET'):
            book_serialize = bookSerializer(book)
            return JsonResponse( book_serialize.data, safe = False, status = status.HTTP_200_OK)

        if(request.method == 'DELETE'):
            book.delete()
            return HttpResponse("The book details has been removed", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            bookdata = JSONParser().parse(request)
            book_serialize = bookSerializer(book, data= bookdata)
            if(book_serialize.is_valid()):
                book_serialize.save()
                return JsonResponse(book_serialize.data, status = status.HTTP_200_OK )

    except:
        return HttpResponse("Invalid data", status = status.HTTP_400_BAD_REQUEST)


#Front-End CRUD
@csrf_exempt
def collect(request):
    if(request.method == 'POST'):
        book_serializer = bookSerializer(data= request.POST)

        if(book_serializer.is_valid()):
            book_serializer.save()
            return redirect(showallpage)

        else:
            return HttpResponse("Error in serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to Library Management System!")


@csrf_exempt
def search(request):
    try:
        getbname = request.POST.get("bname")
        getSearch = Books.objects.filter(bname=getbname)
        bok_serialize = bookSerializer(getSearch, many=True)
        return render(request, 'search.html', {"data":bok_serialize.data})

    except:
        return HttpResponse("Invalid")

@csrf_exempt
def update(request):
    try:
        getname = request.POST.get("bname")
        getupdate = Books.objects.filter(bname = getname)
        b_serialize = bookSerializer(getupdate, many=True)
        return render(request, "update.html", {"data":b_serialize.data})

    except:
        return HttpResponse("Invalid data")

@csrf_exempt
def updateaction(request):
    getnewid = request.POST.get("Newid")
    getnewName = request.POST.get("Newname")
    getnewAuthor = request.POST.get("Newauthor")
    getnewdes = request.POST.get("Newdes")
    getnewprice = request.POST.get("Newprice")
    getnewcat = request.POST.get("Newcat")
    bokdata = {"id":getnewid, "bname":getnewName,"author":getnewAuthor,"descrip":getnewdes,"price":getnewprice,"category":getnewcat}
    jsondata = json.dumps(bokdata)

    apilink = "http://127.0.0.1:8000/books/viewone/"+getnewid
    requests.put(apilink, data=jsondata)
    return HttpResponse("Book detail has been updated")

@csrf_exempt
def delete(request):
    try:
        getname = request.POST.get("bname")
        getD = Books.objects.filter(bname = getname)
        n_serialize = bookSerializer(getD, many = True)
        return render(request, 'delete.html', {"data":n_serialize.data})
    except Books.DoesNotExist:
        return HttpResponse("Invalid", status = status.HTTP_400_BAD_REQUEST)

    except:
        return HttpResponse("Somethimg went wrong!")

@csrf_exempt
def delaction(request):
    getnewid = request.POST.get("Newid")
    getnewName = request.POST.get("Newname")
    getnewAuthor = request.POST.get("Newauthor")
    getnewdes = request.POST.get("Newdes")
    getnewprice = request.POST.get("Newprice")
    getnewcat = request.POST.get("Newcat")
    bokdata = {"id":getnewid, "bname":getnewName,"author":getnewAuthor,"descrip":getnewdes,"price":getnewprice,"category":getnewcat}
    jsondata = json.dumps(bokdata)

    apilink = "http://127.0.0.1:8000/books/viewone/"+getnewid
    requests.delete(apilink, data=jsondata)
    return HttpResponse("Book detail has been deleted")


#HTML Pages

def home(request):
    return render(request, 'home.html')

def bookentry(request):
    return render(request, 'addbook.html')

def showallpage(request):
    getdata = requests.get("http://127.0.0.1:8000/books/viewall/").json()
    return render(request, "showpage.html", {"data":getdata})

def searchbook(request):
    return render(request, 'search.html')

def updatebook(request):
    return render(request, 'update.html')

def delbook(request):
    return render(request, 'delete.html')


