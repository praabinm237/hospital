# Generated by Django 5.0.7 on 2024-09-01 17:14

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.CustomUserManager()),
            ],
        ),
    ]
