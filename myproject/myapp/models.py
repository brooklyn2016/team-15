# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    videoname =  models.CharField(max_length=30, default='hi')
    channel = models.IntegerField(default=0)
    #videotag = models.CharField(max_length=30, default='none')

class VideoQueue(models.Model):
    videoID = models.IntegerField(default=0)
    clipduration = models.IntegerField(default=0)
    clipurl = models.CharField(max_length=30, default='frame.png')
    created_at = models.DateTimeField(editable=False, auto_now_add=True)


    