# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 14:47
from __future__ import unicode_literals

import uuid

from django.db import migrations


def set_uuids_model(apps, model):
    base = apps.get_app_config('base')
    model_class = base.get_model(model)
    ids = model_class.objects.values_list('id', flat=True)
    if ids:
        for pk in ids:
            model_class.objects.filter(pk=pk).update(uuid=uuid.uuid4())


def set_uuid_field(apps, schema_editor):
    set_uuids_model(apps, "learningcontainer")


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0179_learningcontainer_uuid'),
    ]

    operations = [
        migrations.RunPython(set_uuid_field),
    ]
