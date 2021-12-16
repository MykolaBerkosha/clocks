"""
Django settings for clocks project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from pathlib import Path

from djrunner import setup_settings


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i#3&y%*+74bf*+6!)-#t=6zuhpvxasp8le6*i37%(gjn518gm4'
BASE_DIR = Path(__file__).resolve().parent.parent
DB_NAME = 'clocks'

MANAGERS = (
    ('Dev', 'kolya@gmail.com'),
)


# Application definition

INSTALLED_APPS = [
    'core.suit.SuitConfig',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djassets',
    'widget_tweaks',
    'pagination',
    'sorl.thumbnail',
    'watermarks',
    'ordered_model',
    'slider',
    'notify',
    'ckeditor',

    'apps.cart',
    'apps.categories',
    'apps.orders',
    'apps.reviews',
    'apps.products',
    'availability',
    'accounts'
]

STATIC_APPS = [
    'jquery',
    'fa'
]

BOWER_COMPONENTS = [
    'bootstrap#5.0.1'
]

STYLESHEETS = [
    'bower_components/bootstrap/dist/css/bootstrap.css',
]

JAVASCRIPT = [
    'bower_components/bootstrap/dist/js/bootstrap.js',
    'js/custom.js'
]

setup_settings(globals())
