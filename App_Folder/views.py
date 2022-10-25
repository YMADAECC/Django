from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import App_Folder
from django.views.generic.edit import CreateView

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    model = App_Folder
    success_url = reverse_lazy('App_Folder:App_Folder_create_complete')
    
def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'App_Folder_HTML/index.html',context=params)
    