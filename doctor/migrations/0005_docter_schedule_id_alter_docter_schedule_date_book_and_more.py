# Generated by Django 4.1 on 2022-12-15 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_doctor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='docter_schedule',
            name='id',
            field=models.BigAutoField(auto_created=True, default=False, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docter_schedule',
            name='Date_Book',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='docter_schedule',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]