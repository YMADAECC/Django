from django.contrib import admin
from django.urls import path
# Include関数をインポート
from django.urls import include

# path関数でApp_Folder内のurls.pyを読み込むために、include関数を記述
urlpatterns = [
    path('admin/', admin.site.urls),                    # 管理画面のPath
    path('App_Folder/', include('App_Folder.urls')),    # アプリケーション管理フォルダのurls.pyと関連づけるpath
]
