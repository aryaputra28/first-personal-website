from django.shortcuts import render, redirect
from django.http import HttpResponse

def utama(request):
    return render(request,'story8/story8.html')
