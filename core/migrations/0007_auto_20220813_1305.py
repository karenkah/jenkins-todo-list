# Generated by Django 2.1.7 on 2022-08-13 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220813_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 13, 13, 5, 56, 332596)),
        ),
    ]
