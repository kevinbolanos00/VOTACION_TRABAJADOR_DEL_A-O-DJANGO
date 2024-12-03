from django import forms
from .models import Trabajador, Voto

class VotoForm(forms.ModelForm):
    documento_votante = forms.CharField(max_length=20, label="Documento del votante")
    trabajador_candidato = forms.ModelChoiceField(
        queryset=Trabajador.objects.filter(antiguedad__gte=3.0).exclude(tipo_empleado__icontains="SINDICALIZADO-CONVENCIONADO"),
        label="Candidato"
    )

    class Meta:
        model = Voto
        fields = ['trabajador_candidato', 'documento_votante', 'cualidad']
