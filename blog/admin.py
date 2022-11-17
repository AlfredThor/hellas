from django.contrib import admin
from blog import models as blog_model
from django.db import models
from mdeditor.widgets import MDEditorWidget


class Article_Admin(admin.ModelAdmin):
    # order_by
    ordering = ['id']
    # 分页
    list_per_page = 20
    # 显示的字段
    list_display = [
        'id', 'title', 'intro', 'image', 'content_text', 'create_time', 'number', 'like_number'
    ]
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

admin.site.register(blog_model.Article, Article_Admin)


class Sort_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_per_page = 30
    list_display = [
        'id', 'name'
    ]

admin.site.register(blog_model.Sort, Sort_Admin)


class Ip_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_per_page = 30
    list_display = [
        'id', 'ip', 'count', 'visit_time', 'location'
    ]

admin.site.register(blog_model.Ip, Ip_Admin)


class Site_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_per_page = 30
    list_display = [
        'id', 'name', 'site', 'remark','create_time'
    ]

admin.site.register(blog_model.Friend_site, Site_Admin)


# class MoreInfo(admin.TabularInline): #横向显示
#     model=blog_model.Article


class Like_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_per_page = 30
    list_display = [
        'id', 'create_time'
    ]
    # inlines = [MoreInfo]

admin.site.register(blog_model.Like_number, Like_Admin)