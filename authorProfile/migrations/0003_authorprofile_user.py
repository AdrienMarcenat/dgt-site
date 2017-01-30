# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20161231_1714'),
        ('authorProfile', '0002_remove_authorprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorprofile',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='article.User'),
        ),
    ]