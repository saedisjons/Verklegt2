# Generated by Django 4.0.4 on 2022-05-04 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_buyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='buyer',
        ),
    ]
