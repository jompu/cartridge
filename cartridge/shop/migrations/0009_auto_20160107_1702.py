# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20160107_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mh_service_point_meta',
            field=models.CharField(max_length=254, verbose_name='Matkahuolto service point meta', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='mh_service_point',
            field=models.CharField(max_length=254, verbose_name='Matkahuolto service point', blank=True),
        ),
    ]
