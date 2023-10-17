from django.db import models


# Create your models here.
class Pertsona(models.Model):
    izena = models.CharField(max_length=100)
    emaila = models.CharField(max_length=100)
    nan = models.CharField(max_length=9)
    sortu_data = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.izena

class Etxea(models.Model):
    izena = models.CharField(max_length=100)
    herria = models.CharField(max_length=100)
    pertsona_kopurua = models.IntegerField()
    sortu_data = models.DateTimeField(auto_now_add=True)
    alokatu_hasi = models.DateTimeField()
    alokatu_bukatu = models.DateTimeField()
    egoera = models.CharField(max_length=100)
    pertsona = models.ForeignKey(Pertsona, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.izena