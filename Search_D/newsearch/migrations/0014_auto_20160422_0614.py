# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0013_auto_20160420_0801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsolrdata',
            old_name='varient_description',
            new_name='variant_description',
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='image_url',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='slug',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='newsolrdata',
            name='thumbnail_image_url',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
