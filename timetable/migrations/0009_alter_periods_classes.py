# Generated by Django 3.2.18 on 2023-07-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_classes_periods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periods',
            name='Classes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Classes', to='timetable.classes'),
        ),
    ]
