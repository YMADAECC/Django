from django.db import models
from django.utils import timezone
import uuid

class Person(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)


##日記テーブル
class NippoModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    content = models.TextField(max_length=1000, verbose_name="内容")
    public = models.BooleanField(default=False, verbose_name="公開する")
    slug = models.SlugField(max_length=20, unique=True)
