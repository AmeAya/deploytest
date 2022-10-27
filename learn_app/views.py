from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def homeView(request):
    return render(request,
                  template_name='learn_app/home.html',
                  context={
                      'contents': Content.objects.all().order_by('create_date'),
                      'categories': Category.objects.all().order_by('title')
                  })

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

@login_required(login_url='sign_in')
def profile(request):
    return render(request,
                  template_name='learn_app/profile.html',
                  context={
                      'userInfo': LearnUser.objects.get(user_id=request.user.pk),
                      'categories': Category.objects.all().order_by('title')
                  })

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

def homeByCategory(request, category_id):
    return render(request,
                  template_name='learn_app/home.html',
                  context={
                      'contents': Content.objects.filter(category=category_id).order_by('create_date'),
                      'categories': Category.objects.order_by('title')
                  })

def contentDetail(request, content_id):
    return render(request,
                  template_name='learn_app/content_detail.html',
                  context={
                      'categories': Category.objects.order_by('title'),
                      'content': Content.objects.get(pk=content_id)
                           })

@login_required(login_url='sign_in')
def subscriptionHistory(request):
    return render(request,
                  template_name='learn_app/subscription_info.html',
                  context={
                      'categories': Category.objects.order_by('title'),
                      'subscriptions': Subscription.objects.filter(user_id=request.user.pk),
                  })
