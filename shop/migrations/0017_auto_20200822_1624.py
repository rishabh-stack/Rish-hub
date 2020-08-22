# Generated by Django 3.0.8 on 2020-08-22 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200822_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderupdate',
            name='datestamp',
        ),
        migrations.AddField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
