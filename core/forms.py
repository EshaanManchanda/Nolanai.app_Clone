from django import forms
from multiselectfield import MultiSelectFormField
from .models import Scripts, GENRE_CHOICES


class ScriptForm(forms.ModelForm):
    class Meta:
        model = Scripts
        fields = ['title', 'Plot']
