# Generated by Django 3.2.18 on 2023-12-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0033_activecourse_full'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activecourse',
            name='full',
            field=models.BooleanField(),
        ),
    ]
