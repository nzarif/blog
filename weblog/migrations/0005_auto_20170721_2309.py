# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0004_auto_20170721_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=10),
        ),
    ]
