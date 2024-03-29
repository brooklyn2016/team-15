# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('videoname', models.CharField(default=b'hi', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VideoQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoID', models.IntegerField(default=0)),
                ('clipdurations', models.IntegerField(default=0)),
            ],
        ),
    ]
