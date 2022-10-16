from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    information = {
        "Admin_id" : "Database Login"
    }
    return render(request, 'index.html', information)

def dashboard(request):
    return render(request, 'dashboard.html')

def view(request):
    return HttpResponse("This is view page")

def edit(request):
    return HttpResponse("This is edit page")