# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-13 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dojos',
            new_name='Dojo',
        ),
        migrations.RenameModel(
            old_name='ninjas',
            new_name='Ninja',
        ),
    ]
