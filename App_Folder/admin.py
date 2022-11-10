## adminサイト（管理サイト）設定

from django.contrib import admin
from App_Folder.models import Person
from .models import NippoModel

admin.site.register(Person)
admin.site.register(NippoModel)
