from django.shortcuts import render, redirect
from contatos.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Salvo com Sucesso')

    return render(
        request,
        'contato/register.html',
        {
            'form': form
        }
    )