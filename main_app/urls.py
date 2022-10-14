from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('callback/', views.callbackView, name='callback'),
    path('makeCallback/', views.makeCallbackView, name='makeCallback'),
    path('courseDetail/<str:title>/', views.courseDetailView, name='courseDetail'),
]
