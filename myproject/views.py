from django.shortcuts import render
from django.http import HttpResponse
from.models import Image

# Create your views here.

def home(request):
    return HttpResponse("<h1>hello<h1>")


def main(request):
    data = Image.objects.all()
    return render(request,"main.html",{"data": data})

def group(request):
    return render(request,"group.html")

def indian(request):
    return render(request,"indian.html")


