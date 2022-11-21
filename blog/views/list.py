from django.views.generic import ListView
from blog.models import Article


class List(ListView):
    '''时间正序'''
    model = Article
    paginate_by = 15
    context_object_name = 'result'
    ordering = 'id'
    page_kwarg = 'page'
    template_name = 'list.html'

    @property
    def page_number(self):
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        return page

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(List, self).get_context_data(**kwargs)
        content['search'] = {k:v for k,v in self.request.GET.items() if k if v}
        return content

    def get_queryset(self):
        search_data = {}
        title = self.request.GET.get('title', '')
        if title:
            search_data['title'] = title

        content = Article.objects.filter(**search_data).all().order_by('create_time')

        return content