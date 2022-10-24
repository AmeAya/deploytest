from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('signUp/', TemplateView.as_view(template_name='learn_app/registration.html'), name='sign_up'),
    path('createUser/', createUser, name='create_user'),
    path('signUpUserInfo/', TemplateView.as_view(template_name='learn_app/registration_info.html'), name='sign_up_user_info'),
    path('createUserInfo/', createUserInfo, name='create_user_info'),
    path('profile/', profile, name='profile'),
    path('logOut/', logOut, name='log_out'),
    path('signIn/', TemplateView.as_view(template_name='learn_app/login.html'), name='sign_in'),
    path('logIn/', logIn, name='log_in'),
    path('', homeView, name='learn_home'),
]
