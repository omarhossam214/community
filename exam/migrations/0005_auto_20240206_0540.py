# Generated by Django 3.2.18 on 2024-02-06 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20240206_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupilreaction',
            name='selected_answers',
        ),
        migrations.AddField(
            model_name='pupilreaction',
            name='selected_answers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.answer'),
        ),
    ]