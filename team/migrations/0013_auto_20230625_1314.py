# Generated by Django 3.2.18 on 2023-06-25 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_img'),
        ('team', '0012_auto_20230625_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.staff'),
        ),
    ]
