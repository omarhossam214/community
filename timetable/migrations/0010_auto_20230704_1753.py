# Generated by Django 3.2.18 on 2023-07-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_alter_periods_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='days',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='classes',
            name='numberOfPeriods',
            field=models.PositiveIntegerField(null=True),
        ),
    ]