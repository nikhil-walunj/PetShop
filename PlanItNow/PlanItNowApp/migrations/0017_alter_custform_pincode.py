# Generated by Django 5.1.4 on 2025-01-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanItNowApp', '0016_custform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custform',
            name='pinCode',
            field=models.IntegerField(),
        ),
    ]
