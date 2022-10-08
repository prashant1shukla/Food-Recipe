from django.forms import ModelForm
from .models import recipe
from django import forms

class UploadRecipeForm(ModelForm):
    class Meta:
        model = recipe
        fields = "__all__"
        widgets = {'ingredient':forms.Textarea(),'How_to_make':forms.Textarea(),
                   'created_by':forms.HiddenInput()}