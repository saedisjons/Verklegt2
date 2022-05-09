# Generated by Django 4.0.4 on 2022-05-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_logo_user_profile_image_user_fullname_and_more'),
        ('items', '0006_alter_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
