# Generated by Django 3.2.18 on 2024-02-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20240206_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]