# Generated by Django 4.0.4 on 2022-05-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='buyer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
