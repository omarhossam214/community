# Generated by Django 3.2.18 on 2023-12-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0047_alter_staff_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]