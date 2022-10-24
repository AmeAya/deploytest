from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Course, Post


# Create your views here.
def homeView(request):
    return render(request, template_name='main_app/home.html', context={
        'courses': Course.objects.all(),
        'posts': Post.objects.all()
    })


def callbackView(request):
    return render(request, template_name='main_app/callback.html', context={
        'courses': Course.objects.all()
    })


@csrf_exempt
def makeCallbackView(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        if len(email) < 1:
            newStudent = Student(last_name=lastName,
                                 first_name=firstName,
                                 phone=phoneNumber
                                 )
        else:
            newStudent = Student(last_name=lastName,
                                 first_name=firstName,
                                 email=email,
                                 phone=phoneNumber
                                 )
        newStudent.save()
    return redirect(homeView)


def courseDetailView(request, title):
    return render(request, template_name='main_app/courseDetail.html', context={
        'courses': Course.objects.all(),
        'thisCourse': Course.objects.get(title=title)
    })


def backOfficeView(request):
    return render(request, template_name='main_app/backOffice.html', context={
        'courses': Course.objects.all(),
        'callbackRequests': Student.objects.all()
    })


def deleteStudentView(request, pk):
    return render(request, template_name='main_app/deleteStudent.html', context={
        'courses': Course.objects.all(),
        'thisStudent': Student.objects.get(pk=pk),
    })


def deleteStudent(request, pk):
    Student.objects.get(pk=pk).delete()
    return redirect(backOfficeView)

def updateStudentView(request, pk):
    return render(request, template_name='main_app/updateStudent.html', context={
        'courses': Course.objects.all(),
        'thisStudent': Student.objects.get(pk=pk),
    })


def updateStudent(request, pk):
    Student.objects.filter(pk=pk).update(
        first_name=request.POST.get('firstName'),
        last_name=request.POST.get('lastName'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone')
    )
    return redirect(backOfficeView)
