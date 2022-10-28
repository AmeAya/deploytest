from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def homeView(request):
    context = {
        'contents': Content.objects.all().order_by('create_date'),
        'categories': Category.objects.all().order_by('title'),
    }
    if request.user.is_authenticated:
        context['thisUser'] = LearnUser.objects.get(user_id=request.user)
    return render(request,
                  template_name='learn_app/home.html',
                  context=context)

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
                      'userInfo': LearnUser.objects.get(user_id=request.user.pk)
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
                  template_name='learn_app/home_by_category.html',
                  context={
                      'contents': Content.objects.filter(category=category_id).order_by('create_date')
                  })

def contentDetail(request, content_id):
    return render(request,
                  template_name='learn_app/content_detail.html',
                  context={
                      'content': Content.objects.get(pk=content_id)
                  })

@login_required(login_url='sign_in')
def purchaseHistory(request):
    return render(request,
                  template_name='learn_app/purchase_history.html',
                  context={
                      'purchases': PurchaseHistory.objects.filter(user_id=request.user.pk).order_by('-purchase_time')
                  })

def subscriptionsList(request):
    return render(request,
                  template_name='learn_app/subscriptions.html',
                  context={
                      'subscriptions': Subscription.objects.all().order_by('duration_month')
                  })

def subscribe(request, subscription_id):
    user = LearnUser.objects.get(user_id=request.user.id)
    purchase = PurchaseHistory(user_id=user,
                               purchase_time=datetime.now(),
                               subscribe=Subscription.objects.get(id=subscription_id),
                               cost=Subscription.objects.get(id=subscription_id).price
                               )
    purchase.save()
    expire_date = datetime.now() + relativedelta(months=Subscription.objects.get(id=subscription_id).duration_month)

    return redirect(homeView)
