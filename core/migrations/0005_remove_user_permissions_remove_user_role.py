# Generated by Django 5.0.7 on 2024-09-07 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]