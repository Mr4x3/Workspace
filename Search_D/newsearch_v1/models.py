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

class ProductsAttributes(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    ascii_ignd_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products_attributes'

class ProductsCategoryattributesmapping(models.Model):
    value_constraint = models.TextField(blank=True, null=True)
    attr_type = models.CharField(max_length=255, blank=True, null=True)
    is_mandatory = models.IntegerField()
    is_spec = models.IntegerField()
    is_varing = models.IntegerField()
    is_filter = models.IntegerField()
    is_dropdown = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    for_base = models.IntegerField()
    for_subscribed = models.IntegerField()
    attribute = models.ForeignKey(ProductsAttributes, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    change_log_id = models.TextField(blank=True, null=True)
    filter_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Products_categoryattributesmapping'
        unique_together = (('category_id', 'attribute'),)

class ProductsProductcategoryattributesmapping(models.Model):
    subscribed_ref_id = models.CharField(max_length=20, blank=True, null=True)
    text_value = models.TextField(blank=True, null=True)
    int_value = models.IntegerField(blank=True, null=True)
    decimal_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    category_attribute_id = models.IntegerField(blank=True, null=True)
    subscribed_product_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products_productcategoryattributesmapping'
        unique_together = (('subscribed_product_id', 'category_attribute_id'),)

class ProductsProductcategoryattributesmappingfilters(models.Model):
    subscribed_ref_id = models.CharField(max_length=20, blank=True, null=True)
    text_value = models.CharField(max_length=100, blank=True, null=True)
    int_value = models.IntegerField(blank=True, null=True)
    decimal_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    base_product_id = models.IntegerField(blank=True, null=True)
    category_attribute_id = models.IntegerField(blank=True, null=True)
    subscribed_product_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products_productcategoryattributesmappingfilters'
        unique_together = (('base_product_id', 'subscribed_product_id', 'category_attribute_id'),)

class ProductsProducttaxmastermapping(models.Model):
    base_product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Products_producttaxmastermapping'

class AdminFunctions(models.Model):
    title = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255, blank=True, null=True)
    controller_name = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    is_menu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_functions'

class AdminUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    status = models.IntegerField()
    auth_key = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField()
    last_login = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_user'

class Attribute(models.Model):
    attribute_id = models.IntegerField()
    attribute_type = models.CharField(max_length=45, blank=True, null=True)
    attribute_code = models.CharField(max_length=45, blank=True, null=True)
    attribute_name = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    is_searchable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'attribute'

class AttributesData(models.Model):
    base_product_id = models.IntegerField()
    subscribed_product_id = models.IntegerField()
    category_id = models.IntegerField()
    variant = models.CharField(max_length=255, blank=True, null=True)
    variant_value = models.CharField(max_length=255, blank=True, null=True)
    key_features = models.TextField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    uom1 = models.CharField(max_length=255, blank=True, null=True)
    uom2 = models.CharField(max_length=255, blank=True, null=True)
    combo = models.TextField(blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    slug = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attributes_data'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

# class Banners(models.Model):
#     id = models.IntegerField()
#     cat_id = models.IntegerField()
#     type = models.CharField(max_length=255)
#     image_url = models.CharField(max_length=255)
#     status = models.IntegerField()
#     link = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'banners'
#

class BaseProduct(models.Model):
    base_product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    small_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    unit_of_measurement_one = models.CharField(max_length=150, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    key_features = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    status = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    brand_id = models.IntegerField()
    unit_of_measurement_two = models.CharField(max_length=150, blank=True, null=True)
    is_no_follow = models.IntegerField(blank=True, null=True)
    thumb_url = models.CharField(max_length=500, blank=True, null=True)
    base_ref_id = models.CharField(max_length=10, blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    default_category = models.IntegerField()
    combo_categories = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    is_installation_required = models.IntegerField()
    installation_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    installation_moq = models.IntegerField(blank=True, null=True)
    installation_unit_of_measurement = models.CharField(max_length=255, blank=True, null=True)
    additional_text = models.TextField(blank=True, null=True)
    extra_material_required = models.IntegerField()
    extra_material_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    business_unit = models.TextField(blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    brand_type = models.CharField(max_length=255, blank=True, null=True)
    standard_packing_uom = models.CharField(max_length=255, blank=True, null=True)
    unit_quantity_uom = models.CharField(max_length=255, blank=True, null=True)
    purchase_price_uom = models.CharField(max_length=255, blank=True, null=True)
    installation_uom = models.CharField(max_length=255, blank=True, null=True)
    installation_with_material_uom = models.CharField(max_length=255, blank=True, null=True)
    classifications = models.CharField(max_length=255, blank=True, null=True)
    categoryids = models.TextField(blank=True, null=True)
    sub_sub_category = models.CharField(max_length=255, blank=True, null=True)
    video_link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_product'

class Brand(models.Model):
    store_front_id = models.AutoField(primary_key=True)
    store_front_name = models.CharField(max_length=255, blank=True, null=True)
    store_front_api_key = models.CharField(max_length=100, blank=True, null=True)
    store_front_api_password = models.CharField(max_length=100, blank=True, null=True)
    store_front_api_token = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    parent_id = models.IntegerField()
    tagline = models.CharField(max_length=255)
    is_tagline = models.IntegerField()
    redirect_url = models.TextField(blank=True, null=True)
    seller_mailer_flag = models.IntegerField()
    buyer_mailer_flag = models.IntegerField()
    vendor_coupon_prefix = models.CharField(max_length=10)
    order_prefix = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'brand'

class CartValue(models.Model):
    session_id = models.CharField(max_length=50)
    user_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    store_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    store_offer_price = models.DecimalField(max_digits=20, decimal_places=0)
    product_qty = models.IntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=50, decimal_places=0)
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cart_value'

class CatSolrBackLog(models.Model):
    category_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cat_solr_back_log'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    spli_category_id = models.IntegerField()
    category_name = models.CharField(max_length=255)
    parent_category_id = models.IntegerField()
    level = models.IntegerField()
    path = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    is_mega_category = models.SmallIntegerField()
    category_shipping_charge = models.IntegerField()
    status = models.IntegerField()
    cat_tax_per = models.DecimalField(max_digits=5, decimal_places=2)
    cat_banner_img = models.CharField(max_length=255)
    cat_pro_img = models.CharField(max_length=255)
    display_order = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    display_in_menu = models.IntegerField()
    category_icon = models.CharField(max_length=255, blank=True, null=True)
    category_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

class Category2(models.Model):
    category_id = models.AutoField(primary_key=True)
    spli_category_id = models.IntegerField()
    category_name = models.CharField(max_length=255)
    parent_category_id = models.IntegerField()
    level = models.IntegerField()
    path = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    is_mega_category = models.SmallIntegerField()
    category_shipping_charge = models.IntegerField()
    status = models.IntegerField()
    cat_tax_per = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'category2'

# class CategoryShippingCharge(models.Model):
#     id = models.IntegerField()
#     cat_id = models.IntegerField()
#     price = models.IntegerField()
#     shipping_charge = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'category_shipping_charge'
#

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class FilterProductMapping(models.Model):
    product_id = models.IntegerField()
    filter = models.ForeignKey('Filters')
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'filter_product_mapping'

class Filters(models.Model):
    subcategory_id = models.IntegerField()
    name = models.CharField(max_length=255)
    list_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'filters'

# class FinalTable(models.Model):
#     id = models.IntegerField()
#     orderid = models.CharField(max_length=50)
#     subscribed_product_id = models.IntegerField()
#     product_title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=12, decimal_places=4)
#     discount = models.IntegerField()
#     coupon = models.CharField(max_length=50)
#     checkout_price = models.DecimalField(max_digits=12, decimal_places=4)
#     storefront = models.CharField(max_length=255)
#     store = models.CharField(max_length=255)
#     category = models.CharField(max_length=255)
#     user_name = models.CharField(max_length=255)
#     user_email = models.CharField(max_length=255)
#     user_phone = models.IntegerField()
#     user_address = models.CharField(max_length=255)
#     user_pincode = models.IntegerField()
#     timestamp = models.DateTimeField()
#     total_discount = models.FloatField()
#     total_payable_amount = models.FloatField()
#     total_paid_amount = models.FloatField()
#     payment_method = models.CharField(max_length=15)
#     sub_total = models.FloatField()
#     coupon_text = models.CharField(max_length=512)
#     qty = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'final_table'
#

class Logging(models.Model):
    log_id = models.IntegerField()
    user_id = models.CharField(max_length=255)
    entity = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    data = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logging'

class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    media_url = models.CharField(max_length=255, blank=True, null=True)
    thumb_url = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.CharField(max_length=45, blank=True, null=True)
    base_product_id = models.IntegerField()
    variant_id = models.IntegerField()
    is_default = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'media'

# class Mycart(models.Model):
#     id = models.IntegerField()
#     user_id = models.IntegerField(blank=True, null=True)
#     session_id = models.CharField(max_length=55, blank=True, null=True)
#     cart_data = models.CharField(max_length=1111)
#     created_at = models.DateTimeField()
#     modified_at = models.DateTimeField()
#     ip_address = models.CharField(max_length=255)
#     thumb_url = models.TextField(blank=True, null=True)
#     vat = models.IntegerField(blank=True, null=True)
#     moq = models.DecimalField(max_digits=65, decimal_places=2)
#     title = models.CharField(max_length=500, blank=True, null=True)
#     skucode = models.CharField(db_column='SKUCode', max_length=255)  # Field name made lowercase.
#     variant_details = models.CharField(max_length=255, blank=True, null=True)
#     moq_enterprise = models.DecimalField(max_digits=12, decimal_places=4)
#     moq_increment_enterprise = models.DecimalField(max_digits=12, decimal_places=4)
#     moq_enterprise_price = models.DecimalField(max_digits=12, decimal_places=4)
#     moq_sme_price = models.DecimalField(max_digits=12, decimal_places=4)
#     moq_increment_sme = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'mycart'
#

class Newsletter(models.Model):
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'newsletter'

# class NewsletterSubEmailid(models.Model):
#     id = models.IntegerField()
#     email = models.CharField(max_length=255)
#     created_date = models.DateTimeField()
#     modified_date = models.DateTimeField()
#     status = models.IntegerField()
#     ip = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'newsletter_sub_emailid'

class OldStorePriceMapping(models.Model):
    base_product_id = models.IntegerField()
    subscribed_product_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField()
    store_price = models.DecimalField(max_digits=12, decimal_places=4)
    store_offer_price = models.DecimalField(max_digits=12, decimal_places=4)
    lead_time = models.IntegerField()
    publish = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    secondary_store_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'old_store__price_mapping'
        unique_together = (('base_product_id', 'subscribed_product_id', 'store_id'),)

class OrderInvoice(models.Model):
    order_number = models.CharField(max_length=255)
    invoicenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_invoice'

class PincodeMaster(models.Model):
    state = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    region_id = models.IntegerField()
    location = models.CharField(max_length=200, blank=True, null=True)
    publish = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincode_master'
        unique_together = (('pincode', 'location'),)

class Pincodes(models.Model):
    pincode = models.CharField(max_length=25)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pincodes'

class PopularProducts(models.Model):
    mc_id = models.IntegerField()
    sc_id = models.IntegerField()
    base_product_id = models.IntegerField()
    product_title = models.CharField(max_length=255, blank=True, null=True)
    product_image = models.CharField(max_length=255, blank=True, null=True)
    product_slug = models.TextField(blank=True, null=True)
    store_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_store_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    publish = models.IntegerField()
    unit_of_measurement_one = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'popular_products'

class ProductAttributeMapping(models.Model):
    base_product_id = models.IntegerField()
    attribute_id = models.IntegerField()
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_mapping'

class ProductCategoryMapping(models.Model):
    base_product_id = models.IntegerField()
    category_id = models.IntegerField()
    slug = models.CharField(max_length=250, blank=True, null=True)
    base_ref_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_mapping'
        unique_together = (('base_product_id', 'category_id'),)

class ProductFrontendMapping(models.Model):
    subscribed_product_id = models.IntegerField()
    store_front_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_frontend_mapping'

class ProductPincodeMapping(models.Model):
    store_id = models.IntegerField()
    base_product_id = models.IntegerField()
    store_offer_price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    subscribed_product_id = models.IntegerField(blank=True, null=True)
    store_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    region = models.ForeignKey('RegionMasterOld', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pincode_mapping'
        unique_together = (('store_id', 'base_product_id', 'region'),)

class ProductPriceMapping(models.Model):
    base_product_id = models.IntegerField(blank=True, null=True)
    subscribed_product_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_mapping'

class ProductTaxMasterMapping(models.Model):
    base_product_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_tax_master_mapping'

class QuoteFormData(models.Model):
    base_product_id = models.IntegerField()
    subscribed_product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    client_email_id = models.CharField(max_length=255)
    quote_request_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quote_form_data'

class RegionMaster(models.Model):
    name = models.CharField(max_length=255)
    parent_region = models.CharField(max_length=255, blank=True, null=True)
    region_id = models.CharField(max_length=255)
    publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'region_master'

class RegionMasterOld(models.Model):
    name = models.CharField(max_length=255)
    publish = models.IntegerField()
    parent_region = models.CharField(max_length=255, blank=True, null=True)
    region_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region_master_old'

class Responsibilities(models.Model):
    user_id = models.IntegerField()
    admin_func_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'responsibilities'

# class Sessions(models.Model):
#     id = models.CharField(max_length=32)
#     expire = models.IntegerField(blank=True, null=True)
#     data = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sessions'

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
    row_id = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    parent_region_id = models.CharField(max_length=255, blank=True, null=True)
    region_id = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    sub_sub_category=models.CharField(max_length=255, blank=True, null=True)
    brand=models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    synonyms = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=16, blank=True, null=True)
    slug = models.URLField(blank=True, null=True)
    thumbnail_image_url=models.URLField(blank=True, null=True)
    image_url=models.URLField(blank=True, null=True)
    varient_description=models.CharField(max_length=255, blank=True, null=True)
    parent_base_product_id=models.CharField(max_length=255, blank=True, null=True)
    store_price= models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    store_offer_prices= models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
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

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_code = models.CharField(max_length=255, blank=True, null=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    store_details = models.TextField(blank=True, null=True)
    store_logo = models.CharField(max_length=255, blank=True, null=True)
    seller_name = models.CharField(max_length=255, blank=True, null=True)
    business_address = models.CharField(max_length=300, blank=True, null=True)
    business_address_country = models.CharField(max_length=100, blank=True, null=True)
    business_address_state = models.CharField(max_length=100, blank=True, null=True)
    business_address_city = models.CharField(max_length=100, blank=True, null=True)
    business_address_pincode = models.CharField(max_length=100, blank=True, null=True)
    mobile_numbers = models.CharField(max_length=100, blank=True, null=True)
    telephone_numbers = models.CharField(max_length=100, blank=True, null=True)
    visible = models.SmallIntegerField()
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    customer_value = models.DecimalField(max_digits=12, decimal_places=4)
    chat_id = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    tin = models.CharField(max_length=255, blank=True, null=True)
    pan = models.CharField(max_length=255, blank=True, null=True)
    contact_persion_name = models.CharField(max_length=255, blank=True, null=True)
    con_per_mobile = models.CharField(max_length=255, blank=True, null=True)
    con_per_email = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    ac_number = models.CharField(max_length=255, blank=True, null=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    ifsc_code = models.CharField(max_length=255, blank=True, null=True)
    rtgs_code = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    vtiger_status = models.IntegerField()
    vtiger_accountid = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    tagline = models.CharField(max_length=256, blank=True, null=True)
    is_tagline = models.IntegerField()
    store_api_key = models.CharField(max_length=100)
    store_api_password = models.CharField(max_length=100)
    redirect_url = models.TextField(blank=True, null=True)
    seller_mailer_flag = models.IntegerField()
    buyer_mailer_flag = models.IntegerField()
    channel_name = models.CharField(max_length=255)
    channel_id = models.CharField(max_length=255)
    order_prefix = models.CharField(max_length=11)
    is_active_valid = models.IntegerField()
    store_shipping_charge = models.IntegerField()
    store_tax_per = models.FloatField()

    class Meta:
        managed = False
        db_table = 'store'

class StoreFront(models.Model):
    store_front_id = models.IntegerField()
    store_front_name = models.CharField(max_length=255, blank=True, null=True)
    store_front_api_key = models.CharField(max_length=100, blank=True, null=True)
    store_front_api_password = models.CharField(max_length=100, blank=True, null=True)
    store_front_api_token = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    parent_id = models.IntegerField()
    tagline = models.CharField(max_length=255)
    is_tagline = models.IntegerField()
    redirect_url = models.TextField(blank=True, null=True)
    seller_mailer_flag = models.IntegerField()
    buyer_mailer_flag = models.IntegerField()
    vendor_coupon_prefix = models.CharField(max_length=10)
    order_prefix = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'store_front'

class StorePriceMapping(models.Model):
    base_product_id = models.IntegerField()
    subscribed_product_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField()
    store_price = models.DecimalField(max_digits=12, decimal_places=4)
    store_offer_price = models.DecimalField(max_digits=12, decimal_places=4)
    region_id = models.CharField(max_length=255, blank=True, null=True)
    price_type = models.TextField(blank=True, null=True)
    discount = models.DecimalField(max_digits=12, decimal_places=4)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=4)
    markup = models.DecimalField(max_digits=12, decimal_places=4)
    moq_retail = models.DecimalField(max_digits=12, decimal_places=4)
    moq_incremental_retail = models.DecimalField(max_digits=12, decimal_places=4)
    moq_enterprise = models.DecimalField(max_digits=12, decimal_places=4)
    moq_increment_enterprise = models.DecimalField(max_digits=12, decimal_places=4)
    dispatch_location = models.TextField()
    vat = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_charge = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.IntegerField()
    price_validity = models.DateTimeField(blank=True, null=True)
    shipment_mode = models.TextField(blank=True, null=True)
    is_cancelable = models.IntegerField(blank=True, null=True)
    is_cod = models.IntegerField(blank=True, null=True)
    is_returnable = models.IntegerField(blank=True, null=True)
    processing_time = models.TextField(blank=True, null=True)
    conforming_standard = models.TextField(blank=True, null=True)
    warranty = models.TextField(blank=True, null=True)
    item_buying_type = models.CharField(max_length=255, blank=True, null=True)
    publish = models.IntegerField()
    secondary_store_price = models.DecimalField(max_digits=12, decimal_places=2)
    moq_enterprise_price = models.DecimalField(max_digits=12, decimal_places=4)
    moq_sme = models.DecimalField(max_digits=12, decimal_places=4)
    moq_sme_price = models.CharField(max_length=100)
    moq_increment_sme = models.DecimalField(max_digits=12, decimal_places=4)
    max_sme_quantity = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    moq_max_sme = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'store_price_mapping'
        unique_together = (('store_id', 'subscribed_product_id', 'base_product_id', 'region_id'),)

class StoreProductMapping(models.Model):
    subscribed_product_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    base_product_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    expired_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_product_mapping'

# class StoreShippingCharge(models.Model):
#     id = models.IntegerField()
#     store_id = models.IntegerField()
#     price = models.IntegerField()
#     shipping_charge = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'store_shipping_charge'

class StorefrontFbpageMapping(models.Model):
    store_front_id = models.IntegerField()
    page_id = models.CharField(max_length=40)
    page_name = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modify_on = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storefront_fbpage_mapping'

class SubscribedProduct(models.Model):
    subscribed_product_id = models.AutoField(primary_key=True)
    base_product_id = models.IntegerField()
    status = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField()
    is_deleted = models.SmallIntegerField()
    sku = models.CharField(max_length=128)
    quantity = models.IntegerField()
    thumb_url = models.TextField(blank=True, null=True)
    base_ref_id = models.CharField(max_length=200, blank=True, null=True)
    subscribed_ref_id = models.CharField(max_length=200, blank=True, null=True)
    standard_packing_quantity = models.CharField(max_length=255, blank=True, null=True)
    installation_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    installation_sow = models.TextField(blank=True, null=True)
    installation_with_material_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    installation_with_material_sow = models.TextField(blank=True, null=True)
    combo = models.TextField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    installation_moq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribed_product'

class SupplifiedMasterimportupload(models.Model):
    file_name = models.CharField(max_length=500)
    process_name = models.CharField(max_length=300)
    process_type = models.CharField(max_length=50)
    uploaded_on = models.DateTimeField(blank=True, null=True)
    applied_on = models.DateTimeField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    applied = models.IntegerField()
    discarded_on = models.DateTimeField(blank=True, null=True)
    ref_text = models.CharField(max_length=500, blank=True, null=True)
    applied_on_production = models.IntegerField()
    file_path = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser)
    download_query = models.TextField(blank=True, null=True)
    applied_on_production_time = models.DateTimeField(blank=True, null=True)
    sql_error = models.TextField(blank=True, null=True)
    sync_errors = models.TextField(blank=True, null=True)
    sync_query = models.TextField(blank=True, null=True)
    master_category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplified_masterimportupload'

class SyncLog(models.Model):
    last_sync_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sync_log'

class TaxMaster(models.Model):
    category_id = models.IntegerField()
    getit_category_id = models.IntegerField()
    category_name = models.CharField(max_length=255)
    parent_category_id = models.IntegerField()
    level = models.IntegerField()
    path = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    is_mega_category = models.SmallIntegerField()
    category_shipping_charge = models.IntegerField()
    status = models.IntegerField()
    cat_tax_per = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tax_master'

class TempBp(models.Model):
    base_product_id = models.IntegerField()
    title = models.CharField(max_length=255)
    small_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    unit_of_measurement_one = models.CharField(max_length=150, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    key_features = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    status = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    brand_id = models.IntegerField()
    unit_of_measurement_two = models.CharField(max_length=150, blank=True, null=True)
    is_no_follow = models.IntegerField(blank=True, null=True)
    thumb_url = models.CharField(max_length=500, blank=True, null=True)
    base_ref_id = models.CharField(max_length=10, blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    default_category = models.IntegerField()
    combo_categories = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    is_installation_required = models.IntegerField()
    installation_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    installation_moq = models.IntegerField(blank=True, null=True)
    installation_unit_of_measurement = models.CharField(max_length=255, blank=True, null=True)
    additional_text = models.TextField(blank=True, null=True)
    extra_material_required = models.IntegerField()
    extra_material_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    business_unit = models.TextField(blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    brand_type = models.CharField(max_length=255, blank=True, null=True)
    standard_packing_uom = models.CharField(max_length=255, blank=True, null=True)
    unit_quantity_uom = models.CharField(max_length=255, blank=True, null=True)
    purchase_price_uom = models.CharField(max_length=255, blank=True, null=True)
    installation_uom = models.CharField(max_length=255, blank=True, null=True)
    installation_with_material_uom = models.CharField(max_length=255, blank=True, null=True)
    classifications = models.CharField(max_length=255, blank=True, null=True)
    categoryids = models.TextField(blank=True, null=True)
    sub_sub_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_bp'

# class TempProductList(models.Model):
#     id = models.IntegerField()
#     name = models.TextField(blank=True, null=True)
#     pro_name = models.CharField(max_length=255, blank=True, null=True)
#     store_id = models.CharField(max_length=255, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_product_list'

class TestTable(models.Model):
    store_id = models.IntegerField()
    base_product_id = models.IntegerField()
    subscribed_product_id = models.IntegerField()
    region_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_table'
        unique_together = (('base_product_id', 'store_id', 'region_id'),)
