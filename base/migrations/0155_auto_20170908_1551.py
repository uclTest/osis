# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-08 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0154_auto_20170906_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningunityear',
            name='session',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('12', '12'), ('13', '13'), ('23', '23'), ('123', '123'), ('P23', 'P23')], max_length=50, null=True),
        ),
    ]
