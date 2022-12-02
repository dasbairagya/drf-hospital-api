# Generated by Django 4.1.3 on 2022-11-30 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAppointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Appointment date')),
                ('timings', models.CharField(choices=[('9.00–10.00', '9.00–10.00'), ('10.00–11.00', '10.00–11.00'), ('11.00–12.00', '11.00–12.00'), ('12.00–1.00', '12.00–1.00'), ('1.00–2.00', '1.00–2.00'), ('2.00–3.00', '2.00–3.00'), ('3.00–4.00', '3.00–4.00'), ('4.00–5.00', '4.00–5.00'), ('5.00–6.00', '5.00–6.00')], default='9.00–10.00', max_length=20, verbose_name='Appointement time')),
                ('description', models.CharField(max_length=50)),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.register')),
            ],
        ),
    ]
