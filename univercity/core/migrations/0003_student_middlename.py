# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170218_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='middlename',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество'),
        ),
    ]
