# Generated by Django 3.2.18 on 2023-06-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_staff_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
    ]