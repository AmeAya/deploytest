from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Course


# Create your views here.
def homeView(request):
    return render(request, template_name='home.html', context={
        'courses': Course.objects.all()
    })


def callbackView(request):
    return render(request, template_name='callback.html', context={
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
    return render(request, template_name='courseDetail.html', context={
        'courses': Course.objects.all(),
        'thisCourse': Course.objects.get(title=title)
    })
