# Generated by Django 3.2.18 on 2023-12-06 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0018_remove_pupl_periods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activecourse',
            name='capicty',
        ),
        migrations.AddField(
            model_name='activecourse',
            name='capacity',
            field=models.IntegerField(default=5, null=True),
        ),
    ]
