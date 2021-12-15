
import os

from pathlib import Path

from djrunner import setup_settings


SECRET_KEY = 'django-insecure-i#3&y%*+74bf*+6!)-#t=6zuhpvxasp8le6*i37%(gjn518gm4'
BASE_DIR = Path(__file__).resolve().parent.parent
DB_NAME = 'clocks'

MANAGERS = (
    ('Dev', 'kolya@gmail.com'),
)


INSTALLED_APPS = [
    'core.suit.SuitConfig',
    'django.contrib.admin',

    'djassets',
    'widget_tweaks',
    'pagination',
    'watermarks',
    'ordered_model',
    'slider',
    'notify',
    'ckeditor',

    'apps.cart',
    'apps.categories',
    'apps.orders',
    'apps.reviews',
    'apps.products'
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
