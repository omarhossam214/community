# Generated by Django 3.2.18 on 2023-09-17 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0021_auto_20230917_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemperiods',
            name='end_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='coursemperiods',
            name='start_at',
            field=models.DateField(null=True),
        ),
    ]
