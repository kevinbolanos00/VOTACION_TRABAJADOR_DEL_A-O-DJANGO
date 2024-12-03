from django.contrib import admin
from django.db.models import Count
from .models import Voto, Trabajador

# Personalización del modelo Trabajador para el administrador
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'total_votos')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Agregar la anotación de conteo de votos recibidos
        return queryset.annotate(total_votos=Count('votos_recibidos'))

    def total_votos(self, obj):
        # Mostrar el total de votos en la columna
        return obj.total_votos
    total_votos.admin_order_field = 'total_votos'
    total_votos.short_description = 'Número de Votos'

# Registrar los modelos
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Voto)
