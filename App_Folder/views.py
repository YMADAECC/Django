from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from App_Folder.forms import NippoModelForm
from .models import NippoModel
from django.views.generic.edit import CreateView
from django.shortcuts import render

class NippoCreateFormView(CreateView):
    template_name = "App_Folder_HTML\diary_create.html"
    model = NippoModel
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")
    