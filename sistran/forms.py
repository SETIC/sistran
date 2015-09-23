from django import forms
from .models import *


class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        exclude = ['id']
        fields = ('__all__')
