# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from users import  models
from utils import findAppByRP,addUser,findAppByUser

import datetime
# Create your views here.

def index(request):
    if request.session.get('isLogin', False):
        return redirect('/receptor/appointments')
    else:
        return redirect('/receptor/login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['password'] == form.cleaned_data['second_password']:
                form = RegisterForm()
                return render(request, 'receptor/register.html', {'form': form, 'error_message': '两次密码输入不一致!'})
            else:
                addUser(form)
<<<<<<< HEAD
                return redirect('/receptor/login')
=======
                return HttpResponse('注册成功')
>>>>>>> fd73ce76633372f2b9e0f442082ae1bc4837857b
        else:
            form = RegisterForm()
            return render(request, 'receptor/register.html', {'form': form, 'error_message': '请输入正确信息!'})
    else:
        form = RegisterForm()
        return render(request, 'receptor/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            form = LoginForm()
            return render(request, 'receptor/login.html', {'form': form, 'error_message': '用户名或密码不正确'})
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = models.Adminreceptor.objects.get(loginname=username,password=password)
        if user is not None:
            request.session['userId']=user.id_adminreceptor
            request.session['userName']=user.loginname
            request.session['isLogin']=True
            return redirect('/receptor/')
        else:
            form = LoginForm()
            return render(request, 'receptor/login.html', {'form': form, 'error_message': '用户名或密码不正确'})
    else:
        form = LoginForm()
        return render(request, 'receptor/login.html', {'form': form})


def logout(request):
    del request.session['isLogin']
    del request.session['userId']
    return redirect('/receptor/login')

def showAppoint(request,param1):
    if request.session.get('isLogin',False):
        userId = request.session['userId']
        appointments = findAppByRP(userId)
        if param1 is not None:
            if (param1.lower()=="absent"):
                return render(request, 'receptor/absent.html', {'appointments': appointments,'username':request.session['userName']})
            elif (param1.lower()=='present') :
                return render(request, 'receptor/present.html', {'appointments': appointments,'username':request.session['userName']})
            else:
                return render(request, 'receptor/all.html', {'appointments': appointments,'username':request.session['userName']})
        else:
            return render(request, 'receptor/all.html', {'appointments': appointments,'username':request.session['userName']})
    else:
        form = LoginForm()
        return redirect('/receptor/login', {'form': form, 'error_message': '请登录'})


def confirmAppointment(request):
    if request.session.get('isLogin',False):
        id=request.GET['id']
        appointment=models.Appointment.objects.get(id_appointment=id)
        patient=appointment.id_patient
        bulletin=appointment.id_bulletin
        appointment.ispaid=True
        appointment.registrationtime=datetime.datetime.now()
        appointment.save(force_update=True)

        temp=bulletin.id_doctor_department
        doctor=temp.id_doctor
        department=temp.id_department
        hospital=department.id_hospital
        now=datetime.datetime.now()
        info={'patient':patient,'idOfAppointment':id,'time':bulletin.availabletime,'now':now,'doctor':doctor,'department':department,'hospital':hospital}
        return  render(request,'receptor/printAppointment.html',{'info':info})

def printAppointment(request):
    return render(request,'receptor/printAppointment.html')