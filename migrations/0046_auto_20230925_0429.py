# Generated by Django 3.2.18 on 2023-09-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_img'),
        ('timetable', '0023_auto_20230917_0528'),
        ('team', '0045_auto_20230913_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='periods',
            field=models.ManyToManyField(blank=True, null=True, to='timetable.periods'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]