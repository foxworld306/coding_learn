# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-19 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20170419_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannercourse',
            options={'permissions': (('can_see_banner_course', 'can see banner course'), ('cannot_see_banner_course', 'cannot see banner course')), 'verbose_name': '\u8f6e\u64ad\u8bfe\u7a0b', 'verbose_name_plural': '\u8f6e\u64ad\u8bfe\u7a0b'},
        ),
    ]
