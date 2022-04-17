from django import views
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"sample.html")
def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add:int=x+y
    sub:int=x-y
    mul:int=x*y
    div:int=x/y
    return render(request,"result.html",{'result':add,'rsult':sub,'reslt':mul,'rslt':div})
