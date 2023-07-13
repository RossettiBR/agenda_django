from django.shortcuts import render
from contatos.forms import ContatoForms


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContatoForms(request.POST)
        }

    context = {
        'form': ContatoForms()
    }

    return render(
        request,
        'contato/create.html',
        context
    )
