# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorProfile', '0001_squashed_0003_authorprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
    ]
