# Generated by Django 4.2.9 on 2024-07-01 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_commnets_count_blog_comments_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 1, 19, 23, 14, 927828)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 19, 23, 14, 927828)),
        ),
    ]
