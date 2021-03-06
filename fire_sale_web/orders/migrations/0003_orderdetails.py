# Generated by Django 4.0.4 on 2022-05-12 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0013_alter_item_user'),
        ('orders', '0002_paymentdetails_cvv'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, default=None, null=True)),
                ('confirmed', models.BooleanField()),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contactInfo', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.contactinfo')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.paymentdetails')),
            ],
        ),
    ]
