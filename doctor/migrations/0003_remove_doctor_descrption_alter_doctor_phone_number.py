# Generated by Django 4.1 on 2022-12-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_descrption_doctor_email_doctor_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='descrption',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, default='None', max_length=20, null=True),
        ),
    ]
