# Generated by Django 3.0.13 on 2021-12-09 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='code',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='color',
        ),
    ]