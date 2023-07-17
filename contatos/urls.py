# type:ignore
from django.urls import path
from contatos import views

app_name = 'contato'

urlpatterns = [
    path('contato/<int:contact_id>/detail/', views.contato, name='contato'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('contato/create/', views.create, name='create'),
    path('contato/<int:contact_id>/update/', views.update, name='update'),
    path('contato/<int:contact_id>/delete/', views.delete, name='delete'),
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]
