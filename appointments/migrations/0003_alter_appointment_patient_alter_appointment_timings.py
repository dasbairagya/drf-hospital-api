# Generated by Django 4.1.3 on 2022-11-21 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        ('appointments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='timings',
            field=models.CharField(choices=[('09:00–10:00', '09:00–10:00'), ('10:00–11:00', '10:00–11:00'), ('11:00–12:00', '11:00–12:00'), ('12:00–01:00', '12:00–01:00'), ('01:00–02:00', '01:00–02:00'), ('02:00–03:00', '02:00–03:00'), ('03:00–04:00', '03:00–04:00'), ('04:00–05:00', '04:00–05:00'), ('05:00–06:00', '05:00–06:00')], default='09:00–10:00', max_length=20, verbose_name='Appointement time'),
        ),
    ]
