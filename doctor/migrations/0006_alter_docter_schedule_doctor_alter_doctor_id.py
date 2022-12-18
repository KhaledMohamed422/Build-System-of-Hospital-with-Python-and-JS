# Generated by Django 4.1.3 on 2022-12-16 13:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_docter_schedule_id_alter_docter_schedule_date_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docter_schedule',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]