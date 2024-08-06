# Generated by Django 5.0.7 on 2024-07-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_rename_contact_info_patient_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
    ]