# Generated by Django 3.0.5 on 2020-04-26 04:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200425_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
