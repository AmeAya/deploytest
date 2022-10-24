from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.
def homeView(request):
    return render(request, template_name='learn_app/home.html')

def createUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,
                                        password=password)
        user.save()
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('sign_up_user_info')

def createUserInfo(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        user = LearnUser(user_id=request.user,
                         last_name=last_name,
                         first_name=first_name,
                         email=email,
                         phone=phone_number
                         )
        user.save()
        return redirect(homeView)

def profile(request):
    return render(request,
                  template_name='learn_app/profile.html',
                  context={'userInfo': LearnUser.objects.get(user_id=request.user.pk)})

def logOut(request):
    logout(request)
    return redirect(homeView)

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect(homeView)
        else:
            return redirect('sign_in')
