# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:29:30 2022

@author: haruna
"""
from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    ]
