# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20160418_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FilePathField(match='.*\\.img$', path='/books/static/images/'),
        ),
    ]