# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0012_auto_20160420_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='solrdata',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterUniqueTogether(
            name='solrdata',
            unique_together=set([('id', 'region_id')]),
        ),
    ]
