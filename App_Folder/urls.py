#path関数をインポート
from django.urls import path
from .views import NippoCreateFormView

urlpatterns = [
    path("create/", NippoCreateFormView.as_view(), name="nippo-create"),
]