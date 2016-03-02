# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cartridge.shop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150527_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='weight',
            field=models.IntegerField(help_text='Set the relevance of products with the weight.', null=True, verbose_name='Weight', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(help_text='Define primary order with weight.', null=True, verbose_name='Weight', blank=True),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option3',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Property'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option4',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='productoption',
            name='type',
            field=models.IntegerField(verbose_name='Type', choices=[(1, 'Size'), (2, 'Colour'), (3, 'Property'), (4, 'Order')]),
        ),
    ]
