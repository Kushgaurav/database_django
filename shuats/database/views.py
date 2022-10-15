from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is shuats data base")
def view(request):
    return HttpResponse("This is view page")
def edit(request):
    return HttpResponse("This is edit page")