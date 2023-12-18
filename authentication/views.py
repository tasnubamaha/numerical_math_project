from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['confirm-password']

        if password != conpassword:
            messages.error(request=request, message="Passwords did not matched!")
            return

        myuser:User = User.objects.create_user(
            username= username,
            email= email,
            password= password,
        )

        myuser.save()

        messages.success(request=request, message="Sign Up Complete! Redirecting...")

        return redirect("signin")   
    print("method is "+ request.method)

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request,username=username,password=password)

        if user is not None:
            login(request=request,user=user)
            return render(request, "index.html",{'username': user.get_username})
        else:
            messages.error(request=request, message="Bad Credentials")
            return redirect('home')
    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect("home")

def settings(request):
    return render(request, "settings.html")