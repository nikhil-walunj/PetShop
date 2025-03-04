# Generated by Django 5.1.4 on 2024-12-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='petFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petFoodId', models.IntegerField()),
                ('petFoodName', models.CharField(max_length=100)),
                ('petFoodPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('petFoodDesc', models.TextField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
