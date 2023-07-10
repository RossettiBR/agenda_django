from django.urls import path
from contatos import views

app_name = 'contato'

urlpatterns = [
    path('', views.index, name='index'),
]
