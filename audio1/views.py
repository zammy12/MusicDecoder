from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return render(request,'audio1/1.html')