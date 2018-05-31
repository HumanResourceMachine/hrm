from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test(request):
    return render(request, "test.html")