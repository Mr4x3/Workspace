from haystack.forms import SearchForm

class NewSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()