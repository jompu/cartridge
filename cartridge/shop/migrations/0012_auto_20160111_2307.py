# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_mh_card_loaded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_method',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_card_loaded',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_service_point_full',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mh_service_point_id_name',
        ),
    ]
