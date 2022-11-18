# Generated by Django 4.1.3 on 2022-11-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Appointment date')),
                ('timings', models.CharField(choices=[('09:00–10:00', '09:00–10:00'), ('10:00–11:00', '10:00–11:00'), ('11:00–12:00', '11:00–12:00'), ('12:00–1:00', '12:00–1:00'), ('1:00–2:00', '1:00–2:00'), ('2:00–3:00', '2:00–3:00'), ('3:00–4:00', '3:00–4:00'), ('4:00–5:00', '4:00–5:00'), ('5:00–6:00', '5:00–6:00')], default='09:00–10:00', max_length=20, verbose_name='Appointement time')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]