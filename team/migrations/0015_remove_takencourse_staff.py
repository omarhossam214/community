# Generated by Django 3.2.18 on 2023-06-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0014_auto_20230625_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takencourse',
            name='staff',
        ),
    ]
