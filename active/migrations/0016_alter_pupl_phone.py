# Generated by Django 3.2.18 on 2023-12-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active', '0015_auto_20231025_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupl',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]