# Generated by Django 5.1.4 on 2025-01-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanItNowApp', '0013_petproduct_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='petproduct',
            name='delete_details',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
