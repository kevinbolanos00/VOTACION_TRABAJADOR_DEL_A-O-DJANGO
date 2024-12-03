from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    centro_costo = models.IntegerField(null=True)
    ingreso = models.DateField(null=True)
    antiguedad = models.FloatField(null=True)
    ultima_fecha_ingreso = models.DateField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    cargo = models.CharField(max_length=255, null=True)
    tipo_empleado = models.CharField(max_length=255, null=True)
    documento = models.CharField(max_length=20, unique=True, null=True)  # Número de documento único

    def __str__(self):
        return self.nombre


class Voto(models.Model):
    votante = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name="votos_realizados", null=True)
    candidato = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name="votos_recibidos", null=True)
    fecha_voto = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.votante.nombre} votó por {self.candidato.nombre}"