# Generated by Django 5.0.7 on 2024-08-06 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_emergencycase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='contact_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='contact_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='contact_number',
            new_name='phone_number',
        ),
    ]
