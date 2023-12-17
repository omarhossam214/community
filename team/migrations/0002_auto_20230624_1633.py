# Generated by Django 3.2.18 on 2023-06-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='certifcation',
            field=models.ImageField(blank=True, null=True, upload_to='staff_images/'),
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='facebook',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='overview',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
