# Generated by Django 3.2.18 on 2024-02-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20240206_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupilreaction',
            name='degree',
        ),
        migrations.AddField(
            model_name='pupilreaction',
            name='is_correct',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
