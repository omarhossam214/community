# Generated by Django 3.2.18 on 2023-06-25 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_img'),
        ('team', '0019_remove_takencourse_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takencourse',
            name='student',
        ),
        migrations.AddField(
            model_name='takencourse',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.staff'),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]