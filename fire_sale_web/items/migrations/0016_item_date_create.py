# Generated by Django 4.0.4 on 2022-05-13 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_delete_itemoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]