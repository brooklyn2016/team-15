# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='videoname',
            field=models.CharField(default=b'hi', max_length=30),
        ),
    ]
