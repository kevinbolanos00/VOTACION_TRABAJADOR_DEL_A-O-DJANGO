# votacion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Trabajador, Voto

def votar(request):
    if request.method == 'POST':
        documento_votante = request.POST.get('documento')
        id_candidato = request.POST.get('candidato_id')

        # Validar que el votante existe
        votante = get_object_or_404(Trabajador, documento=documento_votante)

        # Verificar si ya votó
        if Voto.objects.filter(votante=votante).exists():
            messages.error(request, "Ya has votado anteriormente.")
            return redirect('votar')  # Aquí aseguramos usar el espacio de nombres

        # Validar que el candidato existe
        candidato = get_object_or_404(Trabajador, id=id_candidato)

        # Registrar el voto
        Voto.objects.create(votante=votante, candidato=candidato)
        messages.success(request, f"¡Tu voto para {candidato.nombre} ha sido registrado exitosamente!")
        return redirect('votar')  # Aquí también usamos el espacio de nombres

    # Si es GET, mostrar los candidatos
    votante = None
    if 'documento' in request.GET:
        votante = Trabajador.objects.filter(documento=request.GET['documento']).first()

    # Obtener todos los trabajadores con antigüedad mayor o igual a 3.0
    trabajadores = Trabajador.objects.all()
    candidatos = trabajadores.exclude(id=votante.id) if votante else trabajadores
    candidatos = candidatos.filter(antiguedad__gte=3.0)  # Filtro por antigüedad

    # Filtro por búsqueda de nombre si existe un término
    nombre_busqueda = request.GET.get('buscar_nombre', '').strip()
    if nombre_busqueda:
    # Filtrar por nombre o cargo usando Q para combinar condiciones OR
        from django.db.models import Q
        candidatos = candidatos.filter(
            Q(nombre__icontains=nombre_busqueda) | Q(cargo__icontains=nombre_busqueda)
    )

    # Ordenar candidatos por cargo (alfabéticamente) y luego por nombre
    candidatos = candidatos.order_by('cargo', 'nombre')

    # Enumerar los candidatos
    candidatos_enumerados = enumerate(candidatos, start=1)

    return render(request, 'votar.html', {
        'candidatos_enumerados': candidatos_enumerados, 
        'votante': votante,
        'nombre_busqueda': nombre_busqueda,  # Pasar el término de búsqueda al template
    })