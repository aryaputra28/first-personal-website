from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    return render(request, 'herokuapp/index.html')

def page2(request):
    return render(request,'herokuapp/portofolio.html')
