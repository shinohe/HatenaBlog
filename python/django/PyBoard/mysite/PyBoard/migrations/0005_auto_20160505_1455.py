# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyBoard', '0004_auto_20160505_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='register_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='update_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topicdetail',
            name='register_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topicdetail',
            name='update_datetime',
            field=models.DateTimeField(),
        ),
    ]
