# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20180603_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='adress',
        ),
    ]
