# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsearch', '0002_auto_20160413_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSolrData',
            fields=[
                ('id', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_id', models.CharField(blank=True, max_length=255, null=True)),
                ('model_name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('synonyms', models.CharField(blank=True, max_length=255, null=True)),
                ('identifier', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'new_solr_data',
            },
        ),
    ]
