# Generated by Django 3.2.18 on 2024-02-28 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0008_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.CharField(choices=[('attended', 'Attended'), ('cancelled_teacher', 'Cancelled by Teacher'), ('cancelled_student', 'Cancelled by Student')], default='attended', max_length=20),
        ),
    ]