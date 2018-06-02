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

def interview_time(request):
    if request.method == "GET":
        res = {
            "interviews":[
                {
                    "job_title": "Google SDE",
                    "date": "2018-06-03"
                },
                {
                    "job_title": "Amazon SDE",
                    "date":"2018-06-20"
                },{
                    "job_title": "HP SDE",
                    "date":"2018-06-25"
                },{
                    "job_title": "Airbnb SDE",
                    "date":"2018-06-07"
                },
            ]
        }
    else:
        res = {
            "verdict": "ok"
        }
    return JsonResponse(res)

def interview_status(request):
    res = {
        "interviews": [
            {
                "job_title": "Google SDE",
                "status": -4
            },
            {
                "job_title": "HP SDE",
                "status": "4"
            }
        ]
    }
    return JsonResponse(res)

def users(request):
    res = {
        "username": "Yanmei Han",
        "role": "2",
    }
    return JsonResponse(res)