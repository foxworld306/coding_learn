# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-23 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20170419_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(max_length=200, upload_to='course/resource/%Y/%m', verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]