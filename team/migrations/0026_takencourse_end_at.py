# Generated by Django 3.2.18 on 2023-06-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0025_takencourse_start_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='takencourse',
            name='end_at',
            field=models.DateTimeField(null=True),
        ),
    ]
