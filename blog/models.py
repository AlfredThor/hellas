from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User
from django.utils import timezone


class Sort(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增主键')
    name = models.CharField(max_length=10, verbose_name='分类')

    class Mate:
        db_table = 'sort'
        verbose_name = '分类'
        verbose_name_plural = 'sort'
        ordering = ['id']

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增主键')
    title = models.CharField(verbose_name='文章标题', max_length=100)
    intro = models.CharField(max_length=300, verbose_name='文章简介')
    content_text = MDTextField(verbose_name='文章正文')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    number = models.IntegerField(verbose_name='阅读量')
    like_numbers = models.IntegerField(default=0, null=False, verbose_name='点赞量')
    sort = models.ForeignKey(Sort, to_field='id', on_delete=models.CASCADE, verbose_name='分类外键',  db_constraint=False)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, verbose_name='用户外键',  db_constraint=False)

    class Mate:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = 'article'
        ordering = ['id']

    def __str__(self):
        return self.title

    def update_number(self):
        self.number += 1
        self.save(update_fields=['number'])

    def update_like_number(self):
        self.like_number += 1
        self.save(update_fields=['like_number'])


class Ip(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(verbose_name='IP地址', max_length=30)
    count = models.IntegerField(default=0, verbose_name='访问次数')
    visit_time = models.DateField(auto_now=True, verbose_name='访问时间')
    location = models.CharField(verbose_name='IP归属地', max_length=30, default=' ')

    class Mate:
        db_table = 'ip'
        verbose_name = '访问统计'
        verbose_name_plural = 'ip'
        ordering = ['id']

    def update_count(self):
        self.count += 1
        self.save(update_fields=['count'])

    def __str__(self):
        return self.ip


class Friend_site(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增ID')
    name = models.CharField(max_length=64, verbose_name='网站名称')
    site = models.CharField(max_length=128, verbose_name='网址')
    remark = models.CharField(max_length=64, null=True, verbose_name='备注')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Mate:
        db_table = 'friend_site'
        verbose_name = '友链'
        verbose_name_plural = 'friend_site'
        ordering = ['id']


class Like_number(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='')
    ip_id = models.OneToOneField(Ip, to_field='id', on_delete=models.CASCADE, verbose_name='关联ip模型，一对一',  db_constraint=False)
    article_id = models.OneToOneField(Article, to_field='id', on_delete=models.CASCADE, verbose_name='关联USER模型，一对一',  db_constraint=False)
    create_time = models.DateTimeField(default=timezone.now, verbose_name='点赞时间')

    class Meta:
        verbose_name = '用户点赞'
        verbose_name_plural = verbose_name
