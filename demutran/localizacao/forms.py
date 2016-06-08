from django import forms
from .models import *
from django.forms import extras


class TipoLogradouroForm(forms.ModelForm):
    class Meta:
        model=TipoLogradouro
        exclude = ['id']
        fields = ('__all__')


class LogradouroForm(forms.ModelForm):
    class Meta:
        model=Logradouro
        exclude = ['id', 'logradouro']
        fields = ('__all__')


class BairroForm(forms.ModelForm):
    class Meta:
        model=Bairro
        exclude = ['id', 'bairro']
        fields = ('__all__')
        

class MunicipioForm(forms.ModelForm):
    class Meta:
        model=Municipio
        exclude = ['id', 'municipio']
        fields = ('__all__')