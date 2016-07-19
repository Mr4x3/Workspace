/*******************************************************
 * Copyright (C) Rspective Owners
 * More info Vivek@crushus.com
 * This file is part of Search Project.
 * 
 * ##Document Created on 1june 
 * ##Haystack/Django/SOLR
 * Version 2
 *******************************************************/

You can use Haystack to index and search for text in any field in any of the models you have defined in your project.

Haystack doesn't perform the search per se; it works as a bridge between the information in your models/queries in your search forms, and a text search engine/backend. We will show here how to configure Haystack to search in different fields of a single model, using Solr as the search backend.

Preliminaries
Let's assume we have a small CMS application ( cms_base), with a Page model, as follows:


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
        ...

And we want to have a search form that searches in the title, the keyword, the , and the category of the attachment of all the pages available.

Note that we are assuming here that you have already installed Haystack and Solr properly, and that you have configured your Django project to load Haystack.

Indexing your data
The basic procedure to index the data in a model is to:

Define a class that tells Haystack which model to use, how to select the instances of the model to index, and other miscellaneous (an Index class).

Haystack will index one document per model instance. We must provide a template to build such document, given the model instance.
Create the initial index, indexing all the instances of the models configured.
Update periodically the index.
Index class definition

from haystack import indexes
from newsearch.models import SolrData

class SolrDataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='title')
    pub_date = indexes.DateTimeField(model_attr='model_name')
    title = indexes.CharField(model_attr='title')
    ids = indexes.CharField(model_attr='id', faceted=True)
    title1 = indexes.CharField(model_attr='title')
    model = indexes.CharField(model_attr='model_name')
    keywords = indexes.CharField(model_attr='keywords')
    category = indexes.CharField(model_attr='category')
    slug = indexes.CharField(model_attr='slug')

    def get_model(self):
        return SolrData
    
    def get_updated_field(self):
        return 'updated'

    def index_queryset(self, using=None):
        #makink index from command line
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


The search engines that Haystack uses are built around the idea of documents: you feed them a document (a bunch of plain text), and some sort of ID for the document, and when searching they will give you back the matched documents IDs.

The declaration of the text field in this class is basically telling Haystack that this is the "main" or default field to perform search upon (document=True), and that we will use a template (yes, a regular Django template) to build that document (use_template=True).

Take into account that the field declarations of this class have nothing to do with the model (Page) fields. You can declare fields that take their data from a model field, but it isn't required to search the instance contents. Also, the field names in the Index class don't have to match the field names in the model class. Finally, it is a common (Haystack) practice to use the text name for the field that defines the main document, so you should not change it if you can help it.

The get_model method simply tells Haystack what model instances we are going to index.

NOTE: Haystack will detect and load automatically all the classes in the search_indexes.py file of all the applications of your project (in this case, cms_base); if you need to index/search other models, just define the class in the corresponding search_indexes.py file, and you're good to go.

Document template definition
The Index class will look for a template to build the document, according to the following schema, in any of the template directories of your Django project:

search/indexes/<APP_NAME>/<MODEL_NAME>_<INDEX_FIELD>.txt

like we have search/templates/search/indexes/newsearch/solrdata_text.txt
In our example, we'll create the following file:

This template should build a simple text file, with all the text that you want to index for your model instance. Right now, we will index the title, content, and author fields. To do so, write your template as follows:

{{ object.title|safe }}
{{ object.content|safe }}
{{ object.author.get_full_name }}
As you can see, this is a regular Django template; you can use filters, access attributes, methods, and so on. The model instance will be available in the template as the object variable.

Some things to take into account when writing the template:

Django's default behaviour is to HTML-escape the text it puts in the templates; if you want to get your text as-is, you'll have to use the safe template filter.
Do your best to get only the words you want indexed into the template. This might imply, for example, removing HTML tags from a field that contains HTML text. Template filters like striptags might prove useful.
Indexing contents of attached files
Indexing the content of attached files ( FileFields) takes a bit of extra work; basically you have to:

Extract the text of the file (.DOC, .PDF, .RTF files.)
Make that text available in the template context, so you can put it in the document.
Extracting the text depends heavily on the kind of file you are analyzing, and is rather cumbersome. And, even though most search engines have functionality to do precisely that processing and extraction, this functionality must also be exposed via Haystack to be useful to us.

In the template, we can add the contents of the file like this:

{{ object.title|safe }}
{{ object.content|safe }}
{{ object.author.get_full_name }}
{{ file_data.contents|striptags|safe }}
We use the striptags filter, because of the HTML tags added by the Solr service to the attached file text.

Create the initial version of the index.
After configuring the model and defining the template for each document, we are (almost) ready to index our data. Before doing that, we must generate Solr's schema. Issue the following command:

./manage.py build_solr_schema > schema.xml
put the schema.xml file in Solr's configuration area (/etc/solr/conf/schema.xml in Ubuntu's stock installation of Solr.), and restart the application server that is hosting Solr (Jetty/Tomcat).

Now we can index our model. Issue the following command:

./manage.py rebuild_index
It will check all of the elements of your model and index the text you defined in the template.

Keeping your index up-to-date
Haystack provides us with an update_index command, that lets us check only the most recent elements we have added/modified, and index/reindex them. You can use it as follows:

./manage.py update_index --age=2
the argument to the age parameter tells Haystack to check for elements that have been modified in the last (in this example) 2 hours.

However, to do this, Haystack needs a bit of support in the models it is indexing; there must be a field in the model that keeps track of the last modification date of each instance, and we must tell Haystack which field it is.

In our example, the Page.updated_at field fills this role. To let Haystack know about it, we must override the get_updated_field method of the index class, as follows:

class PageIndex(indexes.SearchIndex, indexes.Indexable):
    ...
    def get_updated_field(self):
        return "updated_at"
Note if we don't provide this field, Haystack will always check all the instances of the model it is indexing when performing an update, regardless of the age parameter.