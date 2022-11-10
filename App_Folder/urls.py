#path関数をインポート
from django.urls import path
from . import views
from .views import NippoCreateFormView

urlpatterns = [
    path("create/", views.NippoCreateFormView.as_view(), name="nippo-create"),
    path("list/", views.NippoCreateFormView.as_view(), name='nippo-list')
]