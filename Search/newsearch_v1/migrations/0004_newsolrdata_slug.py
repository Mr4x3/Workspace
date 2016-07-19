# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0003_newsolrdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsolrdata',
            name='slug',
            field=models.TextField(null=True, blank=True),
        ),
    ]
