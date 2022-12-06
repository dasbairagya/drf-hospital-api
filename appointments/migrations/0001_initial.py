# Generated by Django 4.1.3 on 2022-12-06 14:07

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('disease', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('timings', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('patients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookappointments', to='patients.register')),
            ],
        ),
    ]
