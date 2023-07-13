from django.shortcuts import render
from contatos.forms import ContatoForms


def create(request):
    if request.method == 'POST':
        form = ContatoForms(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            ...

        return render(
            request,
            'contato/create.html',
            context
        )

    context = {
        'form': ContatoForms()
    }

    return render(
        request,
        'contato/create.html',
        context
    )
