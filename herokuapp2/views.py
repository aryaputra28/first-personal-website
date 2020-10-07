from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    return render(request, 'herokuapp2/story1.html')
