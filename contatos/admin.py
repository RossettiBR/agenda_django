from django.contrib import admin
from contatos import models


@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'show',
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 30
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'id', 'phone',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
