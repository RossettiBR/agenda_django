from contatos.models import Contato
from django import forms
from django.core.exceptions import ValidationError


class ContatoForms(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init'
            }
        ),
        label='Primeiro nome',
        help_text='Texto para ajudar seu usuario'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init'
        # })

    class Meta:
        model = Contato
        fields = 'first_name', 'last_name', 'phone',
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui!'
        #         }
        #     )
        # }

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
