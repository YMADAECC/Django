from django import forms
from .models import App_Folder
 
 
class App_FolderForm(forms.ModelForm):
    class Meta:
        model = App_Folder
        fields = ('date', 'title', 'text',)
        
        exclude = ('id', 'created_at', 'upadted_at',)
