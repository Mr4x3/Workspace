from django.utils import timezone
from haystack import indexes
from newsearch.models import SolrData

class SolrDataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #author = indexes.CharField(model_attr='title')
    #author = indexes.CharField(model_attr='title')
    #pub_date = indexes.DateTimeField(model_attr='model_name')
    #title = indexes.CharField(model_attr='title')
    ids = indexes.CharField(model_attr='id', faceted=True)
    title1 = indexes.CharField(model_attr='title')
    model = indexes.CharField(model_attr='model_name')
    keywords = indexes.CharField(model_attr='keywords')
    category = indexes.CharField(model_attr='category')
    slug = indexes.CharField(model_attr='slug')
    title = indexes.EdgeNgramField(model_attr='title')
    #slug = indexes.CharField(model_attr='category')
    #autocomplete
    #content_auto = indexes.EdgeNgramField(model_attr='title')
    #print(keywords)

    def get_model(self):
        return SolrData
    
    def get_updated_field(self):
        return 'updated'

    def index_queryset(self, using=None):
        #makink index from command line
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    #return self.get_model().objects.all()
    #.filter(=timezone.now())
