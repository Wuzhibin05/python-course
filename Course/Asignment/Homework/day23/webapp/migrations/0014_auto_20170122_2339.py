# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_coursescore_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursescore',
            old_name='num',
            new_name='score',
        ),
    ]
