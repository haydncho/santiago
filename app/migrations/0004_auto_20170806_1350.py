# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170806_1341'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='drgs',
            table='diagnosis_related_groups',
        ),
        migrations.AlterModelTable(
            name='indexgroup',
            table='index_group',
        ),
        migrations.AlterModelTable(
            name='servicepackage',
            table='service_package',
        ),
    ]