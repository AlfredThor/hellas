from django.views.generic import ListView
from blog.models import Article
from django.shortcuts import render
from django.views.generic import View


class Index(View):

    def get(self, request):
        return render(request, 'index.html')

# class Index(ListView):
#
#     model = Article
#     paginate_by = 200
#     context_object_name = 'result'
#     ordering = 'id'
#     page_kwarg = 'page'
#     template_name = 'index.html'
#
#     @property
#     def page_number(self):
#         page_kwarg = self.page_kwarg
#         page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
#         return page
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         content = super(Index, self).get_context_data(**kwargs)
#         return content
#
#     # def get_queryset(self):
#     #     search_data = {}
#     #     name = self.request.GET.get('name', '')
#     #     if name:
#     #         search_data['name'] = name
#     #
#     #     content = Article.objects.filter(**search_data).values(
#     #         'id', 'code', 'name', 'create_time', 'auth__ready_name', 'types'
#     #     ).order_by('-id')
#     #     return content
