from django.shortcuts import render

from contatos.models import Contato
from django import forms
from django.core.exceptions import ValidationError


class ContatoForms(forms.ModelForm):
    class Meta:
        model = Contato
        fields = 'first_name', 'last_name', 'phone',

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()
