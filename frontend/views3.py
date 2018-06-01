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

# 以下测试函数
def test_login(request):
    res = {
        "verdict": "ok",
        "message": "hello"
    }
    return JsonResponse(res)

def test_register(request):
    res = {
        "verdict": "ok",
        "message": "hello"
    }
    return JsonResponse(res)

def test_view_job_info(request):
    res = {
        "job_list": [
            {"job": "Hardware Engineer"},
            {"desc": "Design Architecture"}
        ]
    }
    return JsonResponse(res)