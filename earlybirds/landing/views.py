from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request,user)
                return redirect("/profile")
            else:
                return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect("/profile")
            else:
                return redirect("/login")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

def home(request):
    return render(request,'index.html') 

def courses(request):
    return render(request,'courses.html') 

def internships(request):
    return render(request,'internships.html') 

def profile(request):
    return render(request,'profile.html') 

def projects(request):
    return render(request,'projects.html') 

def skill_detail(request):
    return render(request,'skill_detail.html') 

def team(request):
    return render(request,'team.html')

def course_detail(request):
    return render(request,'course_detail.html')

def project_detail(request):
    return render(request,'project_detail.html')  
