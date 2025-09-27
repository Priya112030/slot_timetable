from django.shortcuts import render
from django.http import HttpResponse

def table(request):
    return render(request,'table.html')

def view1(request):
    return render(request,'temp.html')