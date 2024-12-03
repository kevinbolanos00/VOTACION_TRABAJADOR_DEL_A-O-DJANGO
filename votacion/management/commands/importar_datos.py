import pandas as pd
from django.core.management.base import BaseCommand
from votacion.models import Trabajador

class Command(BaseCommand):
    help = 'Importar datos desde un archivo Excel'

    def handle(self, *args, **kwargs):
        file_path = 'K:/DESARROLLO/VOTACION/form/mejorTra/personal2024.xlsx'  # Cambia por la ruta de tu archivo
        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            Trabajador.objects.create(
                nombre=row['APELLIDO Y NOMBRE'],
                centro_costo=row['CENTRO COSTO'],
                ingreso=row['INGRESO'],
                antiguedad=row['ANTIGÜEDAD'],
                ultima_fecha_ingreso=row['ULTIMA FECHA DE INGRESO'],
                fecha_nacimiento=row['FECHA DE NACIMIENTO'],
                cargo=row['CARGO'],
                tipo_empleado=row['TIPO DE EMPLEADO'],
                #documento=row['DOCUMENTO']  # Asegúrate de que exista en el Excel
            )
        self.stdout.write(self.style.SUCCESS('Datos importados con éxito'))