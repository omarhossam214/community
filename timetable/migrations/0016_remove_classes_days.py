# Generated by Django 3.2.18 on 2023-07-05 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0015_alter_classes_numofweek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='days',
        ),
    ]
