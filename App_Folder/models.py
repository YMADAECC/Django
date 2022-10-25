from django.db import models
from django.utils import timezone
import uuid
 
class Person(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)

##日記テーブル
class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    text = models.CharField(verbose_name='本文', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)
