# Generated by Django 4.0.4 on 2022-05-13 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0010_rename_order_rating_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
