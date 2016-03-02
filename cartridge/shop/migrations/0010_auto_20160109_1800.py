# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20160107_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mh_service_point',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_service_point_meta',
        ),
        migrations.AddField(
            model_name='order',
            name='mh_service_point_full',
            field=models.CharField(max_length=254, verbose_name='Matkahuolto service point', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='mh_service_point_id_name',
            field=models.CharField(max_length=254, verbose_name='Matkahuolto service point id and name', blank=True),
        ),
    ]
