from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def greeting(request):
    try:
        return JsonResponse({"message":"Congratulations! You have dockerized your first application."},safe=False)
    except Exception as error:
        print("error",error)