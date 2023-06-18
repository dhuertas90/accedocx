from django import forms
from crispy_forms.helper import FormHelper

from .models import Documento


class DocumentoForm(forms.ModelForm):

    titulo = forms.CharField(label='Título')
    autor = forms.CharField(label='Autor')
    doc = forms.FileField(label='Documento')
    class Meta:
        model = Documento
        fields = ('titulo', 'autor', 'doc')
  