# Generated by Django 3.2.18 on 2023-12-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0032_alter_instructor_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecourse',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
