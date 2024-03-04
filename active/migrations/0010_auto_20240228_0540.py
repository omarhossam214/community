# Generated by Django 3.2.18 on 2024-02-28 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0009_alter_attendance_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='active_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='active.activecourse'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.CharField(choices=[('attended', 'Attended'), ('cancelled_teacher', 'Cancelled by Teacher'), ('cancelled_student', 'Cancelled by Student')], default='attended', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='active.pupl'),
        ),
    ]
