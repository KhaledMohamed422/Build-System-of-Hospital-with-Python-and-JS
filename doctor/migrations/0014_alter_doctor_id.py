# Generated by Django 4.1.3 on 2022-12-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_alter_specialization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]