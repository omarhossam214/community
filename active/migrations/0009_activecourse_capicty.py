# Generated by Django 3.2.18 on 2023-10-01 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0008_alter_activecourse_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecourse',
            name='capicty',
            field=models.IntegerField(null=True),
        ),
    ]
