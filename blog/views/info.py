from django.shortcuts import render
from django.views.generic import View
from django.views.generic import DetailView
from blog.models import Article
import markdown

class Info(View):

    def get(self, *args, **kwargs):
        return render(self.request, 'info.html')

# class Info(DetailView):
#     model = Article
#     template_name = 'info.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'result'
#     query_pk_and_slug = False
#
#     def get_context_data(self, **kwargs):
#         content = super(Info, self).get_context_data(**kwargs)
#         article_obj = Article.objects.filter(id=self.kwargs[self.pk_url_kwarg]).first()
#         article_obj.content = markdown.markdown(article_obj.content_text.replace("\r\n", '  \n'), extensions=[
#             'markdown.extensions.extra',
#             'markdown.extensions.codehilite',
#             'markdown.extensions.toc',
#         ], safe_mode=True, enable_attributes=False)
#         content['article'] = article_obj
#         return content