# Generated by Django 4.2.9 on 2024-06-29 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='commnets_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 29, 17, 42, 13, 802972)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 29, 17, 42, 13, 802972)),
        ),
    ]
