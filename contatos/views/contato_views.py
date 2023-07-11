from django.shortcuts import render
from contatos.models import Contato

# Create your views here.


def index(request):
    contatos = Contato.objects.filter(show=True).order_by('-id')[:20]

    context = {
        'contatos': contatos,
    }

    return render(
        request,
        'contato/index.html',
        context,
    )
