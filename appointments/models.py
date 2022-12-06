from django.db import models
from patients.models import Register


# Create your models here.
class BookAppointments(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False)
    timings = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    patients = models.ForeignKey(Register, related_name='bookappointments', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return '%d - %s' % (self.pk, self.user)
