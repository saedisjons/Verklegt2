# Generated by Django 4.0.4 on 2022-05-13 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_item_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]