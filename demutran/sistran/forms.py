from datetime import date

from django import forms
from .models import *


class PermissaoForm(forms.ModelForm):

    class Meta:
        model = Permissao
        exclude = ['id', 'data']
        fields = ('__all__')


class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        exclude = ['id']
        fields = ('__all__')


class CobradorForm(forms.ModelForm):

    class Meta:
        model = Cobrador
        exclude = ['id']
        fields = ('__all__')


class ProprietarioForm(forms.ModelForm):

    class Meta:
        model = Proprietario
        exclude = ['id']
        fields = ('__all__')


class VeiculoForm(forms.ModelForm):
    COMBUSTIVEL_CHOICES = (
        ('GASOLINA', 'GASOLINA'),
        ('ÁLCOOL', 'ÁLCOOL'),
        ('GNV', 'GNV'),
        ('DIESEL', 'DIESEL'),
    )
    exercicio = forms.ChoiceField(label='Ano de Exercício', choices=[(x, x) for x in range(1990, date.today().year+1)], required=True)
    combustivel = forms.MultipleChoiceField(label='Combustível', required=True, widget=forms.CheckboxSelectMultiple, choices=COMBUSTIVEL_CHOICES)
    ano_fabricacao = forms.ChoiceField(label='Ano de Fabricação', choices=[(x, x) for x in range(1980, date.today().year+1)], required=True)
    ano_modelo = forms.ChoiceField(label='Ano do Modelo', choices=[(x, x) for x in range(1980, date.today().year+2)], required=True)

    class Meta:
        model = Veiculo
        exclude = ['id']
        fields = ('__all__')


class VistoriaForm(forms.ModelForm):

    class Meta:
        model = Vistoria
        exclude = ['id']
        fields = ('__all__')


class OrdemServicoForm(forms.Form):
    permissao = forms.Select(attrs={'class': 'form-control'})
