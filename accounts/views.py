from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request,'Password does not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists')
        else:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            messages.success(request,'Your account has been successfully created')
            return redirect('login')

    return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return render(request,'login.html',{'error' : 'Invalid username or password'})
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    return render(request,'home.html')