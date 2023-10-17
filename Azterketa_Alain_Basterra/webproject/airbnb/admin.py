from django.contrib import admin
from .models import Pertsona, Etxea
# Register your models here.

class PertsonaAdmin(admin.ModelAdmin):
    list_display = ['izena', 'emaila', 'nan']

admin.site.register(Pertsona, PertsonaAdmin)

class EtxeaAdmin(admin.ModelAdmin):
    list_display = ['izena', 'herria','pertsona_kopurua','alokatu_hasi','alokatu_bukatu','egoera','pertsona']

admin.site.register(Etxea, EtxeaAdmin)