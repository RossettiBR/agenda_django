from django.urls import path
from contatos import views

app_name = 'contato'

urlpatterns = [
    path('contato/<int:contact_id>/detail/', views.contato, name='contato'),  # type:ignore
    path('search/', views.search, name='search'),  # type:ignore
    path('', views.index, name='index'),  # type:ignore
]
