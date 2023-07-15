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
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category',
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui!'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'last_name',
                ValidationError(
                    'Primeiro nome não pode ser igual ao sobrenome',
                    code='invalid'
                )
            )

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Primeiro nome não pode ser igual ao sobrenome',
        #         code='invalid'
        #     )
        # )
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add error',
                    code='invalid'
                )
            )
        return first_name
