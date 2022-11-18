from rest_framework import serializers
from appointments.models import Appointment
from patients.models import Patient


class AppointmentSerializer(serializers.Serializer):
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

    id = serializers.IntegerField(read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    disease = serializers.CharField(max_length=50)
    date = serializers.DateField(label="Appointment date",)
    timings = serializers.ChoiceField(label="Appointement time", choices=TIMESLOT_LIST)
    description = serializers.CharField(max_length=100)


    def create(self, validated_data):
        new_appointment = Appointment.objects.create(
            patient=validated_data['patient'],
            disease=validated_data['disease'],
            date=validated_data['date'],
            timings=validated_data['timings'],
            description=validated_data['description'],

        )
        return new_appointment

    def update(self, instance, validated_data):
        instance.patient = validated_data.get('patient', instance.patient)
        instance.disease = validated_data.get('disease', instance.disease)
        instance.date = validated_data.get('date', instance.date)
        instance.timings = validated_data.get('timings', instance.timings)
        instance.description = validated_data.get('description', instance.description)

        instance.save()

        return instance