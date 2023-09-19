from django import forms
from .models import contact

class form(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"