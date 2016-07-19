# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0007_auto_20160419_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsolrdata',
            old_name='model_name',
            new_name='description',
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='image_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='parent_base_product_id',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='parent_region_id',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='store_offer_prices',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='store_price',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='thumbnail_image_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsolrdata',
            name='varient_description',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='region_id',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
    ]
