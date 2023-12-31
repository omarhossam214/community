# Generated by Django 3.2.18 on 2023-12-15 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_img'),
        ('timetable', '0023_auto_20230917_0528'),
        ('active', '0026_auto_20231215_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='staff_images/')),
                ('title', models.CharField(choices=[('instructor', 'instructor'), ('Not intstuctor', 'Not intstuctor')], max_length=100, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('courses', models.ManyToManyField(blank=True, null=True, to='courses.Course')),
                ('periods', models.ManyToManyField(blank=True, null=True, to='timetable.periods')),
            ],
        ),
        migrations.AlterField(
            model_name='activecourse',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='active.instructor'),
        ),
    ]
