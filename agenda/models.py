from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    def __str__(self):
        return self.nome + "(" + self.email + ")"

class Agendas(models.Model):
    visivel = models.BooleanField(max_length=128)
    nome = models.CharField(max_length=128)
    descricacao = models.CharField(max_length=256)
    usuario = models.ForeignKey(Usuario)
    institucional = models.BooleanField(max_length=128)

class Compromissos(models.Model):
    descricacao = models.CharField(max_length=256)
    agendas = models.ForeignKey(Agendas)
    def __str__(self):
        return self.descricacao

class TipoAgenda(models.Model):
    nome = models.CharField(max_length=128)
    agendas = models.ForeignKey(Agendas)

class UsuarioAgenda(models.Model):
    nome = models.CharField(max_length=128)
    agendas = models.ForeignKey(Agendas)

class UsuarioCompromisso(models.Model):
    nome = models.CharField(max_length=128)
    compromisso = models.ForeignKey(Compromissos)
    confirmacao = models.BooleanField(max_length=128)
