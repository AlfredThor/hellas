from django.urls import re_path
from blog.views import about, cover, index, info, list, share, time, life

app_name = 'base'

urlpatterns = [

    # 首页
    re_path('^index/$', index.Index.as_view(), name='index/'),
    # 关于我
    re_path('^about/$', about.About.as_view(), name='about/'),
    # 模板分享
    re_path('^share/$', share.Share.as_view(), name='share/'),
    # 博客日记
    re_path('^list/$', list.List.as_view(), name='list/'),
    # 慢生活
    re_path('^life/$', life.Life.as_view(), name='life/'),
    # 美文欣赏
    re_path('^cover/$', cover.Cover.as_view(), name='cover/'),
    # 时光轴
    re_path('^time/$', time.Time.as_view(), name='time/'),
    # 文章详情页 (?P<id>\d+)
    re_path('^info/(?P<id>\d+)/$', info.Info.as_view(), name='info/'),

]
