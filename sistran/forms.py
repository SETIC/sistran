from django import forms
from .models import *


class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = ('__all__')
