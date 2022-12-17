# Generated by Django 4.1 on 2022-12-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_rename_data_10to12_docter_schedule_data1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='name',
            field=models.CharField(blank=True, choices=[('Diagnostic radiology', 'Diagnostic radiology'), ('Anesthesiology', 'Anesthesiology'), ('Dermatology', 'Dermatology'), ('Blood', 'Blood')], max_length=100, null=True),
        ),
    ]
