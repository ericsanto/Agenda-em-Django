from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .form import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView, LoginRequiredMixin):
  template_name = 'home.html'


class UsuarioCreate(CreateView):
  template_name = 'cadastro.html'
  form_class = UsuarioForm
  success_url = reverse_lazy('login')