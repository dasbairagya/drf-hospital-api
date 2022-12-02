from django.db import models

# Create your models here.
from patients.models import Register


class BookAppointments(models.Model):

    SLOT1 = '9.00–10.00'
    SLOT2 = '10.00–11.00'
    SLOT3 = '11.00–12.00'
    SLOT4 = '12.00–1.00'
    SLOT5 = '1.00–2.00'
    SLOT6 = '2.00–3.00'
    SLOT7 = '3.00–4.00'
    SLOT8 = '4.00–5.00'
    SLOT9 = '5.00–6.00'

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

    patients = models.ForeignKey(Register, on_delete=models.CASCADE, db_column='patients')
    disease = models.CharField(max_length=50)
    date = models.DateField(verbose_name="Appointment date", auto_now=False, auto_now_add=False)
    timings = models.CharField(verbose_name="Appointement time", max_length=20,  choices=TIMESLOT_LIST, default=SLOT1)
    description = models.CharField(max_length=50)

    @property
    def patient_name(self):
        self.patients.get_name

    def __str__(self):
        return  self.patients.get_name
