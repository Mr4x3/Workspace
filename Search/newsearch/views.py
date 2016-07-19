from django.shortcuts import render
from django.shortcuts import render_to_response
import json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter
from haystack.inputs import Raw
from django.core import serializers

class BorkHighlighter(Highlighter):
    # Override Highlighter Class
    def render_html(self, highlight_locations=None, start_offset=None, end_offset=None):
        highlighted_chunk = self.text_block[start_offset:end_offset]
        print(highlighted_chunk)
        for word in self.query_words:
            highlighted_chunk = highlighted_chunk.replace(word, 'Bork!')
        return highlighted_chunk
def NewHighlight(sentence, query, html_tag, css_class):
    #custom highlighter
    start="<%s class='%s'>"%(html_tag,css_class)
    end='</%s>'%(html_tag)
    return sentence.lower().replace(query,start+query+end)

def search_titles(request):
    articles= SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text',''))
    return render_to_response('search/ajax_search.html', {'articles' : articles})

def autocomplete(request):
    #highlight = Highlighter(my_query)
    #highlight.highlight(my_text)
    query=request.GET.get('q', '')
    high=Highlighter(query, html_tag='span', css_class='search_highlighted_text')
    #result=SearchQuerySet().raw_search(text=query)
    #auto= SearchQuerySet().autocomplete(text=request.GET.get('q', ''))
    #product = SearchQuerySet().filter(text=Raw(request.GET.get('q', '')),ids__startswith='p').highlight()
    #brand = SearchQuerySet().filter(text=Raw(request.GET.get('q', '')),ids__startswith='b').highlight()
    #category = SearchQuerySet().filter(text=Raw(request.GET.get('q', '')),ids__startswith='c').highlight()
    product = SearchQuerySet().autocomplete(title=request.GET.get('q', ''),identifier='products')#.highlight()
    brand = SearchQuerySet().autocomplete(title=request.GET.get('q', ''),identifier='brand',)#.highlight()
    category = SearchQuerySet().autocomplete(title=request.GET.get('q', ''),identifier='category')#.highlight()
    #sca=category = SearchQuerySet().autocomplete(title=request.GET.get('q', ''),identifier='sub_sub_category')
    #ca=category = SearchQuerySet().autocomplete(title=request.GET.get('q', ''),identifier='sub_sub_category')
    #high=SearchQuerySet().filter(text=query).highlight()
    #print(auto)
    #suggestions = [result.title for result in auto]
    #print(suggestions)
    print('hello')
    box=[product,brand,category]
    c=0
    for i in box:
        c+=1
        for j in i:
            c+=1
            #print(j.title,str(c))
    #print(box)
    print(product)
    boxstr=['product','brand','category']
    #fieldstr={'title','keywords','category','slug','highlight'}
    flu={}
    count=0
    #RTstr=['title','keywords','category',]
    def check_which_field_match(RT,num):
        c=0
        for i in RT:
            #print(j[num])
            if i[num]:
                if query.lower() in i[num].lower():
                    #print(query , j[num])
                    #print(RTstr[c])
                    #return {RTstr[c]:high.highlight(i[num])[3:]}
                    return {RTstr[c]:NewHighlight(i[num].lower(), query.lower(), 'span', 'search_highlighted_text')}
                else:
                    c=c+1
            else:
                c=c+1
    for _ in [product,brand,category]:
        final=[]
        #text=[dataone.text for dataone in _]
        title=[dataone.title for dataone in _]
        category=[dataone.category for dataone in _]
        sub_category=[dataone.sub_category for dataone in _]
        sub_sub_category=[dataone.sub_sub_category for dataone in _]
        slug=[dataone.slug for dataone in _]
        brand=[dataone.brand for dataone in _]
        thumbnail_image_url=[dataone.thumbnail_image_url for dataone in _]
        RT=[title,category,sub_category,sub_sub_category,slug,brand,thumbnail_image_url,]
        RTstr=['title','category','sub_category','sub_sub_category','slug','brand','thumbnail_image_url',]
        #highlight=[dataone.highlighted.get('text')[0].replace('em>','b>') for dataone in _]
        #highlight=[check_which_field_match(RT,i) for i in range(len(title))]
        #print(highlight)
        for i in range(len(title)):
            final.append({'title':title[i],'category':category[i],'sub_category':sub_category[i],'sub_sub_category':sub_sub_category[i],'slug':slug[i],'brand':brand[i],'thumbnail_image_url':thumbnail_image_url[i],})
        #print(final)
        #flu[boxstr[count]]={'title':title,'keywords':keywords,'category':category,'slug':slug,'highlight':highlight}
        flu[boxstr[count]]=final
        #print({'title':title,'keywords':keywords,'category':category,'slug':slug,'highlight':highlight})
        #print(count)
        #print(boxstr[count])
        count=count+1
    #print(flu)
    #print(type(sqs.highlight()))
    #highlight=[dataone.highlighted.get('text')[0] if dataone.highlighted else None for dataone in high]
    #print(highlight)
    #highlight=[list(k)[0] for k in highlights]
    #print('fd',full_data)
    #queryset=SearchQuerySet().filter(content=request.GET['q'])
    #k=serializers.serialize("json", [x.title for x in sqs])
    #print(k)
    data1=flu
    data=json.dumps(flu)
#    data2 = json.dumps({
#        'title':title,
#        'keywords':keywords,
#        'category':category,
#        'highlight':highlight,
#        'slug':slug
#    })
    return HttpResponse(data, content_type='application/json')
