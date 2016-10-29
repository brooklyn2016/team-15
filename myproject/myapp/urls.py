# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import upload
from myproject.myapp.views import index

urlpatterns = [
    url(r'^upload/$', upload, name='upload'),
    url(r'^index/$', index, name='index'),
]
