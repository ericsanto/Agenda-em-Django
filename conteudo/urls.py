from django.urls import path
from conteudo.views import *



urlpatterns = [
    path('agenda/', produto_list, name='agenda'),
    path('adicionar_novos_contatos', AddContato, name='adicionar_novos_contatos'),
    path('detalhes_contatos/<slug:slug>', DetalhesContatos.as_view(), name='detalhes_contatos'),
    path('update/<contato_id>', updade_contato , name='update'),
    path('delete_contato/<contato_id>', delete_contato , name='delete_contato'),
]