from django.http import JsonResponse
from django.shortcuts import render

def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})  # JSON response
