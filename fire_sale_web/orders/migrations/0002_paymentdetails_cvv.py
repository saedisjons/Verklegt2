# Generated by Django 4.0.4 on 2022-05-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='cvv',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
