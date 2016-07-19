# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0017_remove_newsolrdata_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsolrdata',
            name='identifier',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
