from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def response1(request):
    return HttpResponse("This is one type response i.e. HttpResponse")

def response2(request):
    return render(request,"response2.html")