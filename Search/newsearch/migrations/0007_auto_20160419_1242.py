# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0006_auto_20160419_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsolrdata',
            name='region_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
