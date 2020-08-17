# Generated by Django 3.0.8 on 2020-08-15 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20200815_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
