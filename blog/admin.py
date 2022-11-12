from django.contrib import admin
from blog import models as blog_model
from django.db import models
from mdeditor.widgets import MDEditorWidget


class Article_Admin(admin.ModelAdmin):
    # order_by
    ordering = ['create_time']
    # 分页
    list_per_page = 20
    # 显示的字段
    list_display = [
        'id', 'title', 'intro', 'content_text', 'create_time', 'number', 'like_number'
    ]
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

    # 多对多关系的展示
    # def show_all_sort(self, obj):
    #     return [a.name for a in obj.sort.all()]
    #
    # filter_horizontal = ['sort']


admin.site.register(blog_model.Article, Article_Admin)
