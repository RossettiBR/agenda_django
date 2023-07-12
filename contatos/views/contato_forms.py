from django.shortcuts import get_list_or_404, redirect, render

from contatos.models import Contato


def create(request):
    context = {

    }
    return render(
        request,
        'contato/create.html',
        context
    )
