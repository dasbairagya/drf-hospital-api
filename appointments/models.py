from django.db import models

# Create your models here.
from patients.models import Patient


class Appointment(models.Model):

    SLOT1 = '09:00–10:00'
    SLOT2 = '10:00–11:00'
    SLOT3 = '11:00–12:00'
    SLOT4 = '12:00–01:00'
    SLOT5 = '01:00–02:00'
    SLOT6 = '02:00–03:00'
    SLOT7 = '03:00–04:00'
    SLOT8 = '04:00–05:00'
    SLOT9 = '05:00–06:00'

    TIMESLOT_LIST = [
        (SLOT1, SLOT1),
        (SLOT2, SLOT2),
        (SLOT3, SLOT3),
        (SLOT4, SLOT4),
        (SLOT5, SLOT5),
        (SLOT6, SLOT6),
        (SLOT7, SLOT7),
        (SLOT8, SLOT8),
        (SLOT9, SLOT9),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.CharField(max_length=50)
    date = models.DateField(verbose_name="Appointment date", auto_now=False, auto_now_add=False)
    timings = models.CharField(verbose_name="Appointement time", max_length=20,  choices=TIMESLOT_LIST, default=SLOT1)
    description = models.CharField(max_length=50)

    @property
    def patient_name(self):
        self.patient.get_name

    def __str__(self):
        return  self.patient.get_name
