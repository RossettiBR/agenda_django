from django.shortcuts import render, redirect, get_object_or_404
from contatos.forms import ContatoForms
from django.urls import reverse
from contatos.models import Contato


def create(request):
    form_action = reverse('contato:create')

    if request.method == 'POST':
        form = ContatoForms(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contato:update', contact_id=contact.pk)

        return render(
            request,
            'contato/create.html',
            context
        )

    context = {
            'form': ContatoForms(),
            'form_action': form_action,
    }

    return render(
        request,
        'contato/create.html',
        context
    )


def update(request, contact_id):
    contact = get_object_or_404(Contato, pk=contact_id, show=True)
    form_action = reverse('contato:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContatoForms(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contato:update', contact_id=contact.pk)

        return render(
            request,
            'contato/create.html',
            context
        )

    context = {
            'form': ContatoForms(instance=contact),
            'form_action': form_action,
    }

    return render(
        request,
        'contato/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(Contato, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contato:index')

    return render(
        request,
        'contato/contato.html',
        {
            'contato': contact,
            'confirmation': confirmation,
        }
    )
