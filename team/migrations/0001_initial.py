# Generated by Django 3.2.18 on 2023-06-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='staff_images/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
