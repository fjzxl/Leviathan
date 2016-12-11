import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leviathan.settings")
django.setup()

from users import models
import datetime
import logging
logging.basicConfig()



def task():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    bulletinList = models.Bulletin.objects.filter(availabletime__range=(today, tomorrow))
    leveDict = {'A': 'B', 'B': 'C', 'C': 'x'}
    for k in bulletinList:
        appointmentList = list(models.Appointment.objects.filter(id_bulletin=k.id_bulletin))
        for j in appointmentList:
            patient = j.id_patient
            bulletin = j.id_bulletin
            if j.registrationtime is not None:
                if ((j.registrationtime - bulletin.availabletime).seconds > 0):
                    patient.credit = leveDict[patient.credit]
                else:
                    patient.credit = patient.credit
            else:
                patient.credit = leveDict[patient.credit]
            patient.save()


