# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20160112_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_method',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_service_point_full',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_service_point_id_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_shipment_number',
        ),
    ]
