import pandas as pd
from votacion.models import Trabajador

def cargar_trabajadores():
    archivo_excel = 'ubicación de tu archivo.xlsx'  # Cambia por la ubicación de tu archivo
    datos = pd.read_excel(archivo_excel)

    for _, fila in datos.iterrows():
        Trabajador.objects.create(
            nombre=fila['APELLIDO Y NOMBRE'],
            centro_costo=fila['CENTRO COSTO'],
            ingreso=pd.to_datetime(fila['INGRESO'], format='%d/%m/%Y').date(),
            antiguedad=fila['ANTIGÜEDAD'],
            ultima_fecha_ingreso=pd.to_datetime(fila['ULTIMA FECHA DE INGRESO'], format='%d/%m/%Y').date(),
            fecha_nacimiento=pd.to_datetime(fila['FECHA DE NACIMIENTO'], format='%d/%m/%Y').date(),
            cargo=fila['CARGO'],
            tipo_empleado=fila['TIPO DE EMPLEADO'],
            documento=fila['CEDULA'],  
        )