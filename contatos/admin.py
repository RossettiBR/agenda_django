from django.contrib import admin
from contatos import models


@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    ...
