# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-19 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20161113_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'permissions': (('courseview_all', 'Can see all page'), ('courseview_no', 'cannot see this page')), 'verbose_name': '\u7ae0\u8282', 'verbose_name_plural': '\u7ae0\u8282'},
        ),
    ]
