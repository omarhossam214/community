# Generated by Django 3.2.18 on 2023-06-20 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseDetail', '0006_auto_20230621_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='model',
        ),
        migrations.RemoveField(
            model_name='coursedetails',
            name='module',
        ),
        migrations.AddField(
            model_name='chapter',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='courseDetail.module'),
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courseDetail.curriculum'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courseDetail.curriculum'),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Model',
        ),
    ]