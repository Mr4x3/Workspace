# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0009_auto_20160420_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsolrdata',
            name='model_name',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='store_offer_prices',
            field=models.DecimalField(blank=True, null=True, decimal_places=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='store_price',
            field=models.DecimalField(blank=True, null=True, decimal_places=0, max_digits=11),
        ),
    ]
