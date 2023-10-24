from django import forms
from core.models import *


class ContatoSalvoForm(forms.ModelForm):
  
  class Meta:
    model = ContatoSalvo
    fields = [ 'nome', 'sobrenome', 'numero_de_telefone', 'email', 'categoria', 'slug']