# Haystack-Solr Search Version 2*

Example of Search Query
http://localhost:8000/solr/search/?q=cement
Throws out Valid Json For Search Query

##Dependency:
- [x] haystack
- [x] pysolr
- [x] django
- [ ] django-cors-headers

Run solr as solr5.5/bin/solr start

###Tasks
- [x] Remove Problem With cement mapped to Rainforcement or Reinforcement
- [x] Added support for python3
- [x] Documentation
- [x] Use LRU Cache so that it dont hit DB everytime
- [x] added updated column to check changes made between diffrent instances

# Changes To be Done in urls.py
```python
from newsearch.views import autocomplete

urlpatterns = [
    url(r'^solr/admin/', include(admin.site.urls)),
    #url(r'^searchv1/', include('haystack.urls')),
    url(r'^solr/search/', autocomplete, name='autocomplete')
    #url(r'^search/', 'newsearch.views.search_titles'),

]
```

# Changes To be done in settings.py
1. Add new add in settings ie newsearch
2. Change My Sql Connection ie
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supplifi_ecom_stack2',
        'USER': 'pi',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
Add Haystack Settings as:
```python
HAYSTACK_DEFAULT_OPERATOR = 'AND'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/newrambo'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
```
Django dont allow usage from diffrent domain or same domain with diffrent port so use cross validation package and add following line in settings.py
CORS_ORIGIN_ALLOW_ALL = True


## Steps To Follow:
1. add app to django as above and install haystack {Add that to INSTALLED_APPS }, pysolr, solr 5.5
2. use the schema.xml provided or generate a new using python3 manage.py build_solr_schema > schema.xml
3. create a core with this schema.xml and add that core url in django settings HAYSTACK_CONNECTIONS
4. use python3 manage.py rebuild_index for creating new index
5. for updating index use python3 update_index --age=2 (2 means 2 hours)
