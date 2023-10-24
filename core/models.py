from django.db import models

# Create your models here.
from django.db import models


class Categoria(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome


class ContatoSalvo(models.Model):
  nome = models.CharField('Nome: ', max_length=150)
  sobrenome = models.CharField('Sobrenome:', max_length=150, blank=True, null=True )
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  numero_de_telefone = models.CharField('Telefone: ', max_length=20)
  email = models.EmailField('Email: ', max_length=200, blank=True, null=True)
  slug = models.SlugField(unique=True, null=True)

  def __str__(self):
    return self.nome