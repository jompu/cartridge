# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20151210_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mh_service_point',
            field=models.CharField(max_length=254, blank=True),
        ),
    ]
