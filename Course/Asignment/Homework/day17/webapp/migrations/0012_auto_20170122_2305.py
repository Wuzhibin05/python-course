# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20170120_1149'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestScore',
            new_name='CourseScore',
        ),
    ]
