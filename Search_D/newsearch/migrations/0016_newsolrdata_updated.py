# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0015_remove_newsolrdata_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsolrdata',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
