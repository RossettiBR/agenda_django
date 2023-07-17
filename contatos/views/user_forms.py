from django.shortcuts import render, redirect
from contatos.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Salvo com Sucesso')
            return redirect('contato:login')

    return render(
        request,
        'contato/register.html',
        {
            'form': form
        }
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contato:index')

        messages.error(request, 'Login inválido')

    return render(
        request,
        'contato/login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contato:login')
