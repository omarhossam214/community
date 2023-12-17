# Generated by Django 3.2.18 on 2023-06-20 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseDetail', '0007_auto_20230621_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='module',
        ),
        migrations.AddField(
            model_name='chapter',
            name='module',
            field=models.ManyToManyField(null=True, related_name='chapters', to='courseDetail.Module'),
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='curriculum',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courseDetail.curriculum'),
        ),
        migrations.RemoveField(
            model_name='module',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='module',
            name='curriculum',
            field=models.ManyToManyField(null=True, related_name='modules', to='courseDetail.Curriculum'),
        ),
    ]