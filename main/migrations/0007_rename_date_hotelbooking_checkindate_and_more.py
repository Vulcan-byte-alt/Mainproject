# Generated by Django 5.0.1 on 2024-02-15 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_hotel_resortbooking_resort'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='date',
            new_name='CheckInDate',
        ),
        migrations.RenameField(
            model_name='resortbooking',
            old_name='date',
            new_name='CheckInDate',
        ),
    ]
