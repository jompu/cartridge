# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20160111_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(default='pickup', max_length=254, verbose_name='Delivery method', blank=True, choices=[('pickup', 'Pickup'), ('mh', 'Matkahuolto')]),
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
        migrations.AddField(
            model_name='order',
            name='mh_shipment_number',
            field=models.CharField(default='', max_length=255, verbose_name='Matkahuolto shipment number', blank=True),
        ),
    ]
