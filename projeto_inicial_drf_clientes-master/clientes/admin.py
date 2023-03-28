from clientes.models import Cliente
from django.contrib import admin


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 25
    ordering = ('nome',)

admin.site.register(Cliente, Clientes)

