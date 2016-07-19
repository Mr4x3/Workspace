from django.utils import timezone
from haystack import indexes
from newsearch.models import NewSolrData

class SolrDataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #author = indexes.CharField(model_attr='title')
    #author = indexes.CharField(model_attr='title')
    #pub_date = indexes.DateTimeField(model_attr='model_name')
    #title = indexes.CharField(model_attr='title')
    ids = indexes.CharField(model_attr='id', faceted=True,null=True)
    title1 = indexes.CharField(model_attr='title',null=True)
    #model = indexes.CharField(model_attr='model_name')
    keywords = indexes.CharField(model_attr='keywords',null=True)
    category = indexes.CharField(model_attr='category',null=True)
    sub_category = indexes.CharField(model_attr='sub_category',null=True)
    sub_sub_category = indexes.CharField(model_attr='sub_sub_category',null=True)
    slug = indexes.CharField(model_attr='slug',null=True)
    brand = indexes.CharField(model_attr='brand',null=True)
    thumbnail_image_url = indexes.CharField(model_attr='thumbnail_image_url',null=True)
    description = indexes.CharField(model_attr='description',null=True)
    title = indexes.EdgeNgramField(model_attr='title',null=True)
    identifier = indexes.CharField(model_attr='identifier',null=True)
    #slug = indexes.CharField(model_attr='category')
    #autocomplete
    #content_auto = indexes.EdgeNgramField(model_attr='title')
    #print(keywords)

    def get_model(self):
        return NewSolrData
    
    def get_updated_field(self):
        return 'updated'

    def index_queryset(self, using=None):
        #makink index from command line
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    #return self.get_model().objects.all()
    #.filter(=timezone.now())
