# Generated by Django 3.0.8 on 2020-11-09 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_auto_20201103_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='seasonbotmatchupstats',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
