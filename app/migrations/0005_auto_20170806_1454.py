# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170806_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'DRGs\u7248\u672c\u4fe1\u606f', 'verbose_name_plural': 'DRGs\u7248\u672c\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='version',
            name='desc',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]