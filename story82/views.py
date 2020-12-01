from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

import requests

# Create your views here.
def utama(request):
    return render(request,'story82/story82.html')

def searchBook(request):
    if(request.is_ajax()):
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + request.GET['fname'])
        data = response.json()
        return JsonResponse(data)
