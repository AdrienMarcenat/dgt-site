# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorProfile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorprofile',
            name='user',
        ),
    ]
