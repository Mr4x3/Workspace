# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0018_newsolrdata_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsolrdata',
            name='identifier',
        ),
    ]
