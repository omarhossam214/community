# Generated by Django 3.2.18 on 2023-06-21 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseDetail', '0012_auto_20230621_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='chapter',
        ),
        migrations.AddField(
            model_name='chapter',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courseDetail.module'),
        ),
    ]
