# Generated by Django 3.2.18 on 2023-10-22 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0023_auto_20230917_0528'),
        ('active', '0010_activecourse_enrolled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activecourse',
            name='capicty',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='activecourse',
            name='enrolled',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='pupl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('active', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='active.activecourse')),
                ('periods', models.ManyToManyField(null=True, to='timetable.periods')),
            ],
        ),
    ]