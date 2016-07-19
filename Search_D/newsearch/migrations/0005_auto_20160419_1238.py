# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0004_newsolrdata_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsolrdata',
            name='slug',
            field=models.URLField(null=True, blank=True),
        ),
    ]
