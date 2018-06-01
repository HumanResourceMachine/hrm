from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test(request):
    return JsonResponse({"123":"456"})

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def apply_job(request):
    return render(request, "apply_job.html")

def view_job_info(request):
    return render(request, "view_job_info.html")