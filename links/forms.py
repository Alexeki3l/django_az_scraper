from django import forms
from .models import Link

class AddLinlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)