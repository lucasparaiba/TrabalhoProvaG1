from django.shortcuts import render
from agenda.models import *
from django.http import HttpResponse
def listaAgenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = Agendas.objects.all()
    for Agendas in lista:
        retorno += '</br>Agenda: {}</br>'.format(Agendas.nome)
    return HttpResponse(retorno)

def get_agenda_byID(request,id):
    retorno = "<h1>Agendas</h1>"
    evento = Agendas.objects.get(pk=id)
    retorno += '</br>Agenda: {}</br>'.format(Agendas.nome)
    return HttpResponse(retorno)

def listaAgendainstirucional(request):
    retorno = "<h1>Agenda Instituicional</h1>"
    lista = AgendaInstitucional.objects.all()
    for AgendaInstitucional in lista:
        retorno += '</br>Agenda: {}</br>'.format(AgendaInstitucional.compromisso)
    return HttpResponse(retorno)
# Create your views here.
