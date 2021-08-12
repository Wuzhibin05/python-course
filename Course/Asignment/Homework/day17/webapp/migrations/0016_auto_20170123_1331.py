# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_remove_coursescore_test_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescore',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='coursescore',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.StaffInfo'),
            preserve_default=False,
        ),
    ]