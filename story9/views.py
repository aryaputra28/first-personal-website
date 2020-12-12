from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def loginAkun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("MASUK ELSE")
            messages.error(request,"wrong username or password")

    return render(request,'story9/login.html')



def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {'form': form}
    return render(request,'story9/register.html',context)

def logoutAkun(request):
    logout(request)
    return redirect('/login')