# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cataloginfo',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
