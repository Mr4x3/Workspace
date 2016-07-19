# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class CatSolrBackLog(models.Model):
    category_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_solr_back_log'

class SolrBackLog(models.Model):
    subscribed_product_id = models.IntegerField()
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'solr_back_log'

import datetime

class SolrData(models.Model):
    row_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=11)
    region_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        #managed = False
        db_table = 'solr_data'
        unique_together = (('id', 'region_id'),)

class NewSolrData(models.Model):
    id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    row_id = models.AutoField(primary_key=True)
    region_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    sub_sub_category = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    synonyms = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    parent_base_product_id = models.CharField(max_length=255, blank=True, null=True)
    parent_region_id = models.CharField(max_length=255, blank=True, null=True)
    store_offer_prices = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    store_price = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    thumbnail_image_url = models.CharField(max_length=200, blank=True, null=True)
    variant_description = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table='new_solr_data'

class SolrLogData(models.Model):
    searched_keyword = models.TextField(blank=True, null=True)
    searched_time = models.DateTimeField()
    qtime = models.IntegerField()
    responses = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solr_log_data'
#class ToSearchData(model.model):
#    name = model.TextField(blank=True)
#    keyword=model.CharField(max_length=255)
