# Generated by Django 3.2.18 on 2023-07-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0032_takencourse_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='takencourse',
            name='Student',
            field=models.ManyToManyField(null=True, to='team.Student'),
        ),
    ]
