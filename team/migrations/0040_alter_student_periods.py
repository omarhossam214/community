# Generated by Django 3.2.18 on 2023-07-07 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0019_delete_takencourse'),
        ('team', '0039_student_periods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='periods',
            field=models.ManyToManyField(to='timetable.periods', validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]