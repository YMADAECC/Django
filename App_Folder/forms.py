from django import forms
from .models import NippoModel

class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)
