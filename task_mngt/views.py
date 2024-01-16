from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def task_management(request):
    return render(request,'task_management.html')