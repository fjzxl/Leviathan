# -*- coding: utf-8 -*-
# 功能函数放置在此文件中
from . import models
import datetime
#import pytz
from django.contrib.auth.models import User


def add_user(form):
    data = form.cleaned_data
    patient = models.Patient.objects.create(username=data['username'], password=data['password'],
                                            telephone=data['telephone']
                                            , email=data['email'], name=data['name'], credit='A', gender=data['gender'],
                                            age=data['age']
                                            , createtime=datetime.datetime.now(), idcardnumber=data['idcardnumber'])
    patient.save()
    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                    form.cleaned_data['password'])
    user.save()


def auth_user(form):
    if form.is_valid():
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        # check
        user = models.Patient.objects.filter(username=username, password=password)
        if user:
            return True
        else:
            return False
    else:
        return False


def get_hospitals(city):
    locations = models.Location.objects.filter(city__contains=city)
    hospitals = []
    for location in locations:
        find = models.Hospital.objects.filter(id_location=location.id_location)
        for hospital in find:
            hospitals.append(hospital)
    return hospitals


def get_cities(province):
    provinces = models.Location.objects.filter(province__contains=province)
    cities = []
    for province in provinces:
        cities.append(province.city)
    return cities


# 查询特定医院，特定科室的预约信息
def get_bulletins(department_id):
    bulletins = []
    doctor_departments = models.DoctorDepartment.objects.filter(id_department=department_id)
    for doctor_department in doctor_departments:
        find = models.Bulletin.objects.filter(id_doctor_department=doctor_department.id_doctor_department).first()
        if find.availabletime > pytz.utc.localize(datetime.datetime.now()):
            bulletins.append(find)
    return bulletins


def get_doctors(bulletins):
    doctors = []
    for bulletin in bulletins:
        doctor_department = models.DoctorDepartment.objects.filter(
            id_doctor_department=bulletin.id_doctor_department.id_doctor_department).first()
        doctor = models.Doctor.objects.filter(id_doctor=doctor_department.id_doctor.id_doctor).first()
        doctors.append(doctor)
    return doctors


def get_departments(doctors):
    departments = []
    for doctor in doctors:
        doctor_department = models.DoctorDepartment.objects.filter(id_doctor=doctor.id_doctor).first()
        department = models.Department.objects.filter(
            id_department=doctor_department.id_department.id_department).first()
        departments.append(department)
    return departments


def add_appointment(bulletin, username):
    # 查重
    appointment = models.Appointment.objects.filter(id_bulletin=bulletin).first()
    if appointment:
        return False
    patient = models.Patient.objects.filter(username=username).first()
    appointment = models.Appointment.objects.create(ispaid=0, id_bulletin=bulletin
                                                    , id_patient=patient,
                                                    createtime=pytz.utc.localize(datetime.datetime.now()))
    appointment.save()
    return True


def change_password(newpassword, username):
    models.Patient.objects.filter(username=username).update(password=newpassword)
