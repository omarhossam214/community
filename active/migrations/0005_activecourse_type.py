# Generated by Django 3.2.18 on 2023-08-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0004_rename_course_activecourse_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecourse',
            name='type',
            field=models.CharField(choices=[('online', 'online'), ('On site', 'On site')], default='online', max_length=100, null=True),
        ),
    ]
