# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0011_newsolrdata_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solrdata',
            options={},
        ),
    ]
