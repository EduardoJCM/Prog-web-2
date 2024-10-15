from django import forms
from .models import Municipio

class MunicipioForm(forms.Form):
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), empty_label="Selecciona un municipio")
