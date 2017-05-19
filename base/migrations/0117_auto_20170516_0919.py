# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-16 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0116_auto_20170516_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningcomponent',
            name='acronym',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='learningcomponent',
            name='description',
            field=models.CharField(blank=True, choices=[('LECTURING_COMPLETE', 'LECTURING_COMPLETE'), ('LECTURING_INCOMPLETE', 'LECTURING_INCOMPLETE'), ('PRACTICAL_EXERCISES_COMPLETE', 'PRACTICAL_EXERCISES_COMPLETE'), ('PRACTICAL_EXERCISES_INCOMPLETE', 'PRACTICAL_EXERCISES_INCOMPLETE')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='learningcomponent',
            name='type',
            field=models.CharField(blank=True, choices=[('LECTURING', 'LECTURING'), ('STAGE', 'STAGE'), ('DISSERTATION', 'DISSERTATION'), ('PRACTICAL_EXERCISES', 'PRACTICAL_EXERCISES')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='learningcomponentyear',
            name='hourly_volume_Q1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='learningcomponentyear',
            name='hourly_volume_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
