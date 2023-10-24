from django.shortcuts import render

# Create your views here.
from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from core.models import ContatoSalvo
from .form import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


'''class AgendaView(TemplateView):
  template_name = 'agenda.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['lista_de_contatos'] = ContatoSalvo.objects.all()
    return context'''


def authenticated(view_func):
    def check_authentication(request, *args, **kwargs):
        if request.user.is_authenticated:
            # O usuário está autenticado, então chame a função de visualização original
            return view_func(request, *args, **kwargs)
        else:
            # Redirecione o usuário para a página de login ou para onde você desejar
            return redirect('home')  # Substitua 'nome_da_view_de_login' pela URL da sua página de login

    return check_authentication


@authenticated
def produto_list(request):
  template_name = 'agenda.html'
  objects = ContatoSalvo.objects.all()
  search = request.GET.get('search')
  if search:
    objects = objects.filter(nome__icontains=search)
  context = {'lista_de_contatos': objects}
  return render(request, template_name, context)

@authenticated
def AddContato(request):
  if str(request.method) == 'POST':
    form = ContatoSalvoForm(request.POST)
    if form.is_valid():
      messages.success(request,'Contato salvo')
      form.save()
      form = ContatoSalvoForm()
    else:
      messages.error(request, 'Não foi possível adicionar o contato à agenda')
  else:
    form = ContatoSalvoForm()
  context = {
    'form': form
  }
  return render(request, 'adicionar_novos_contatos.html', context)


class DetalhesContatos(TemplateView, LoginRequiredMixin):
  template_name = 'detalhes_contatos.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    url_slug = self.kwargs['slug']
    contatos = ContatoSalvo.objects.get(slug=url_slug)
    contatos.save()
    context['contatos'] = contatos
    return context
  

@authenticated
def updade_contato(request, contato_id):
    contato = ContatoSalvo.objects.get(pk=contato_id)
    form = ContatoSalvoForm(request.POST or None, instance=contato)
    if form.is_valid():
      form.save()
      return redirect('agenda')
    return render(request, 'update.html', {'contato': contato, 'form': form})


@authenticated
def delete_contato(request, contato_id):
    contato = ContatoSalvo.objects.get(pk=contato_id)
    contato.delete()
    return redirect('agenda')