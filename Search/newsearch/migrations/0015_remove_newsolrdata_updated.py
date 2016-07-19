# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0014_auto_20160422_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsolrdata',
            name='updated',
        ),
    ]
