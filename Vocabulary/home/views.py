from django.shortcuts import render, HttpResponse
from .forms import *


# Create your views here.

def home(request):
    if request.method == 'POST':
        request.session['Username'] = request.POST['Write']
        return HttpResponse("Value: " + request.session['Username'])

    return render(request, 'home/index.html', {'form':cookie()})

def log_in(request):
    if request.method == 'POST':
        response = HttpResponse()              
        if Account.objects.filter(Username=request.POST['Username'], Password=request.POST['Password']):
            return render(request, "home/index.html")
        else:
            return HttpResponse("<script type='text/javascript'>csrftoken = alert('Login fail')</script>")
  
    return render(request, 'home/login.html', {'form' : Login()})

def sign(request):
    if request.method == 'POST':
        if Account.objects.filter(Username=request.POST['Username'], Password=request.POST['Password']):
            return HttpResponse("<script type='text/javascript'>alert('Account is existed')</script>")
        else:
            Sign(request.POST).save()
            return HttpResponse("Registry successfully")

    return render(request, 'home/sign.html', {'form' : Sign()})
