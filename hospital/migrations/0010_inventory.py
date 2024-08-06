# Generated by Django 5.0.7 on 2024-07-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_alter_invoice_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]