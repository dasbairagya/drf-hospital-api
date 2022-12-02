from rest_framework import serializers
from appointments.models import BookAppointments
from patients.models import Register


class AppointmentSerializer(serializers.Serializer):
    SLOT1 = '9.00–10.00'
    SLOT2 = '10.00–11.00'
    SLOT3 = '11.00–12.00'
    SLOT4 = '12.00-1.00'
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

    id = serializers.IntegerField(read_only=True)
    patients = serializers.PrimaryKeyRelatedField(queryset=Register.objects.all(), required=False)
    # print(patients)
    disease = serializers.CharField(max_length=50)
    date = serializers.DateField(label="Appointment date", )
    timings = serializers.ChoiceField(label="Appointement time", choices=TIMESLOT_LIST)
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        new_appointment = BookAppointments.objects.create(
            patients=validated_data['patients'],
            disease=validated_data['disease'],
            date=validated_data['date'],
            timings=validated_data['timings'],
            description=validated_data['description'],
        )
        return new_appointment

    def update(self, instance, validated_data):
        instance.patients = validated_data.get('patients_id', instance.patient)
        instance.disease = validated_data.get('disease', instance.disease)
        instance.date = validated_data.get('date', instance.date)
        instance.timings = validated_data.get('timings', instance.timings)
        instance.description = validated_data.get('description', instance.description)

        instance.save()

        return instance

    class Meta:
        model = Register
        fields = ['patients', 'disease', 'date', 'timings', 'description']