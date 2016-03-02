# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20151109_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(default='pickup', max_length=254, verbose_name='Delivery method', blank=True, choices=[('pickup', 'Pickup'), ('mh', 'Matkahuolto')]),
        ),
        migrations.AddField(
            model_name='order',
            name='mh_service_point',
            field=models.CharField(default='', help_text='You can find your nearest service point from the <a href="https://www.matkahuolto.fi/fi/toimipisteet/toimipistehaku/" target="_blank">service point search</a>. If you don\'t specify the service point, we will send your packet to nearest point.', max_length=254, verbose_name='Matkahuolto service point'),
        ),
    ]
