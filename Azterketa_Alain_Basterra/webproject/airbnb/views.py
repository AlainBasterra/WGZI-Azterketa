from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Etxea, Pertsona
# Create your views here.

def index(request):
    etxeak = Etxea.objects.all
    return render(request, 'index.html', {'etxeak': etxeak})

def etxeak(request):
    etxeak = Etxea.objects.all
    return render(request, 'etxeak.html', {'etxeak': etxeak})

def pertsonak(request):
    pertsonak = Pertsona.objects.all
    return render(request, 'pertsonak.html', {'pertsonak': pertsonak})

#crud etxea
def formaddetxea(request):
    pertsonak = Pertsona.objects.all
    return render(request, 'formaddetxea.html', {'pertsonak': pertsonak})
def addetxea(request):
    izena = request.POST['izena']
    herria = request.POST['herria']
    pertsona_kopurua = request.POST['p_kop']
    alokatu_hasi = request.POST['hasi_data']
    alokatu_bukatu = request.POST['bukatu_data']
    egoera = request.POST['egoera']
    pertsona = Pertsona.objects.get(id=request.POST['id'])
    etxe_berria = Etxea(izena=izena, herria=herria, pertsona_kopurua=pertsona_kopurua, alokatu_hasi=alokatu_hasi, alokatu_bukatu=alokatu_bukatu, egoera=egoera, pertsona=pertsona)
    etxe_berria.save()
    return HttpResponseRedirect(reverse('etxeak'))

def deleteetxea(request, id):
    etxea = Etxea.objects.get(id = id)
    Etxea.delete(etxea)
    return HttpResponseRedirect(reverse('etxeak'))

def formupdateetxea(request,id):
    etxea = Etxea.objects.get(id=id)
    pertsonak = Pertsona.objects.all
    return render(request,'formupdateetxea.html',{'etxea':etxea, 'pertsonak':pertsonak})

def updateetxea(request):
    izena = request.POST['izena']
    herria = request.POST['herria']
    pertsona_kopurua = request.POST['p_kop']
    alokatu_hasi = request.POST['hasi_data']
    alokatu_bukatu = request.POST['bukatu_data']
    egoera = request.POST['egoera']
    pertsona = Pertsona.objects.get(id=request.POST['pertsona_id'])

    etxea = Etxea.objects.get(id=request.POST['id'])
    etxea.izena = izena
    etxea.herria = herria
    etxea.pertsona_kopurua = pertsona_kopurua
    etxea.alokatu_hasi = alokatu_hasi
    etxea.alokatu_bukatu = alokatu_bukatu
    etxea.egoera = egoera
    etxea.pertsona = pertsona
    etxea.save()
    return HttpResponseRedirect(reverse('etxeak'))

#crud pertsona
def formaddpertsona(request):
    return render(request, 'formaddpertsona.html')

def addpertsona(request):
    izena = request.POST['izena']
    emaila = request.POST['emaila']
    nan = request.POST['nan']
    pertsona_berria = Pertsona(izena=izena, emaila=emaila, nan=nan)
    pertsona_berria.save()
    return HttpResponseRedirect(reverse('pertsonak'))

def deletepertsona(request, id):
    pertsona = Pertsona.objects.get(id = id)
    Pertsona.delete(pertsona)
    return HttpResponseRedirect(reverse('pertsonak'))

def formupdatepertsona(request,id):
    pertsona = Pertsona.objects.get(id=id)
    return render(request,'formupdatepertsona.html',{'pertsona':pertsona})

def updatepertsona(request):
    izena = request.POST['izena']
    emaila = request.POST['emaila']
    nan = request.POST['nan']
    pertsona = Pertsona.objects.get(id=request.POST['id'])
    pertsona.izena = izena
    pertsona.emaila = emaila
    pertsona.nan = nan
    pertsona.save()
    return HttpResponseRedirect(reverse('pertsonak'))