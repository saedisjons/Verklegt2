# Generated by Django 4.0.4 on 2022-05-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_contactinfo_user_alter_paymentdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='cardNum',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='cvv',
            field=models.TextField(max_length=255),
        ),
    ]