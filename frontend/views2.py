from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test(request):
    return render(request, "test.html")

def change_time(request):
    return render(request, "change_time.html")

def view_time(request):
    return render(request, "view_time.html")

def view_applicants(request):
    return render(request, "view_applicants.html")

def view_status(request):
    return  render(request, "view_status.html")