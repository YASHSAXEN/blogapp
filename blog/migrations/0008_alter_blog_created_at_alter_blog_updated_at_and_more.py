# Generated by Django 4.2.9 on 2024-07-02 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_contactus_username_alter_blog_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 2, 17, 17, 45, 240527)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 2, 17, 17, 45, 240527)),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 2, 17, 17, 45, 241525)),
        ),
    ]
