from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('callback/', views.callbackView, name='callback'),
    path('makeCallback/', views.makeCallbackView, name='makeCallback'),
    path('courseDetail/<str:title>/', views.courseDetailView, name='courseDetail'),
    path('backOffice', views.backOfficeView, name='backOffice'),
    path('deleteStudent/<int:pk>/', views.deleteStudentView, name='deleteStudent'),
    path('deleteStudentFunc/<int:pk>/', views.deleteStudent, name='deleteStudentFunc'),
    path('updateStudent/<int:pk>/', views.updateStudentView, name='updateStudent'),
    path('updateStudentFunc/<int:pk>/', views.updateStudent, name='updateStudentFunc'),
]
