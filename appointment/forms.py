from django import forms
from .models import appoint

class form(forms.ModelForm):
    class Meta:
        model = appoint
        fields = "__all__"