# Generated by Django 5.0.7 on 2024-09-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
