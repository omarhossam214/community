# Generated by Django 3.2.18 on 2024-02-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_remove_question_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='degree',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
