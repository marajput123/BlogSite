# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-26 19:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 26, 19, 39, 12, 130532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 19, 39, 12, 130532, tzinfo=utc)),
        ),
    ]
