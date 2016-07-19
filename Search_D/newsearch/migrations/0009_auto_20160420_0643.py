# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0008_auto_20160420_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsolrdata',
            name='identifier',
            field=models.CharField(null=True, blank=True, max_length=16),
        ),
    ]
