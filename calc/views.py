from django.shortcuts import render, HttpResponse
from calc.models import Contact
import sys
sys.setrecursionlimit(16385)
from django.contrib import messages

def index(request):
    context ={
        "variable": "I am Dharm and I am great"
    }
    # return HttpResponse("This is homepage")
    return render(request,"index.html", context)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def login(request):
    return render(request,"login.html")

def contact(request):
    if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         contact = Contact(name=name, email=email)
         contact.save()
         messages.success(request, 'Your details have been saved')

    return render(request,"contact.html")

