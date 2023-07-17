from contatos.models import Contato
from django import forms
from django.core.exceptions import ValidationError


class ContatoForms(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Contato
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
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
