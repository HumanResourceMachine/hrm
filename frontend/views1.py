from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test(request):
    return JsonResponse({"123":"456"})
	
def view_applicants_list(request):
    return render(request, "view_applicants_list.html")


def score_applicants(request):
    return render(request, "score_applicants.html")


def edit_applicants_workflow(request):
    return render(request, "edit_applicants_workflow.html")


def release_job(request):
    return render(request, "release_job.html")