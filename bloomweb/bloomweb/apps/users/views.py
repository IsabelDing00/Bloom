import pymysql
from django.shortcuts import render,redirect
from django.views import View
from . import models

def registerView(request):
    """User Registion"""
    error_name = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_list = models.User.objects.filter(username=user)
        if user_list:
            error_name = '%sThe username is already exist.' % user
            return render(request,'register.html',{'error_name':error_name})
        else:
            user = models.User.objects.create(username=user,
                                              password=password,
                                              email=email)
            user.save()
    return render(request, 'register.html')

def LoginView(request):
    error_name = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        user_list = models.User.objects.filter(username=user)
        if user_list:
            error_name = '%sThe username is already exist.' % user
            return render(request, 'register.html', {'error_name': error_name})
        else:
            user = models.User.objects.create(username=user,
                                              password=password,
                                              email=email)
            user.save()
    return render(request,'login.html')
