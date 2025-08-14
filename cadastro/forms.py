from django import forms
from .models import NumeroTelefone

class NumeroTelefoneForm(forms.ModelForm):
    class Meta:
        model = NumeroTelefone
        fields = ['numero']
