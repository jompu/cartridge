# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20160109_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mh_card_loaded',
            field=models.BooleanField(default=False),
        ),
    ]
