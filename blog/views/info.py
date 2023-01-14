from django.views.generic import DetailView
from blog.models import Article
import markdown


class Info(DetailView):
    model = Article
    template_name = 'info.html'
    pk_url_kwarg = 'id'
    context_object_name = 'result'
    query_pk_and_slug = False

    def get_context_data(self, **kwargs):
        content = super(Info, self).get_context_data(**kwargs)
        article_obj = Article.objects.filter(id=self.kwargs[self.pk_url_kwarg]).first()
        extensions = [
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            # 自动生成目录
            'markdown.extensions.toc',
            'markdown.extensions.extra',
            'markdown.extensions.abbr',
            'markdown.extensions.attr_list',
            'markdown.extensions.def_list',
            'markdown.extensions.fenced_code',
            'markdown.extensions.footnotes',
            'markdown.extensions.md_in_html',
            'markdown.extensions.tables',
            'markdown.extensions.admonition',
            'markdown.extensions.codehilite',
            'markdown.extensions.legacy_attrs',
            'markdown.extensions.legacy_em',
            'markdown.extensions.meta',
            'markdown.extensions.nl2br',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
            'markdown.extensions.toc',
            'markdown.extensions.wikilinks'
        ]
        article_obj.content_text = markdown.markdown(
            article_obj.content_text.replace("\r\n", '  \n'),
            extensions=extensions, safe_mode=True, enable_attributes=False)
        content['article'] = article_obj
        # print(article_obj.content_text)
        return content