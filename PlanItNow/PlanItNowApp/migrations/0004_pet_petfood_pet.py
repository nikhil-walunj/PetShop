# Generated by Django 5.1.4 on 2024-12-31 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanItNowApp', '0003_petfooddetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petName', models.CharField(max_length=100)),
                ('petCat', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='petfood',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='PlanItNowApp.pet'),
        ),
    ]
