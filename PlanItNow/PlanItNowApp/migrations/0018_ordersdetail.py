# Generated by Django 5.1.4 on 2025-02-05 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanItNowApp', '0017_alter_custform_pincode'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ordersdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('orderDate', models.DateTimeField(auto_now_add=True)),
                ('productstatus', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlanItNowApp.petproduct')),
            ],
        ),
    ]
