# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20170127_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientinfo',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientinfo',
            name='qq',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]