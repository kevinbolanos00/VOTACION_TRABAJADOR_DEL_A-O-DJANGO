# Sistema de Votación al Trabajador del Año

Este proyecto está diseñado para una empresa en la cual el personal activo puede participar votando por el Trabajador del Año. A continuación, se describen los requisitos y las instrucciones para configurar y utilizar el sistema.

---

## **Requerimientos del Sistema**
1. **Carga de Trabajadores Activos:**
   - Los datos del personal activo deben cargarse desde un archivo Excel llamado `personal2024.xlsx`, el cual se incluye en este repositorio.
   - Es importante utilizar este archivo y modelo para asegurar la correcta integración con la base de datos.

2. **Criterios de Candidatos:**
   - Solo los trabajadores que tengan **tres o más años** de antigüedad podrán ser candidatos al Trabajador del Año.
   - Los demás trabajadores solo podrán participar como votantes.

3. **Restricciones de Votación:**
   - Los votantes deben ingresar su número de documento para validar su identidad.
   - Cada votante podrá registrar su voto **una sola vez**.

---

## **Instrucciones para Cargar los Trabajadores**

### **Paso 1: Preparar el Ambiente**
Asegúrese de que el entorno de desarrollo está configurado correctamente y que la base de datos está lista para recibir los datos.

### **Paso 2: Ejecutar el Script de Carga**
Para cargar los datos del archivo `personal2024.xlsx` en la base de datos, siga estos pasos desde el terminal:  
1. Abra el shell de Django:
   ```bash
   python manage.py shell
   from votacion.scripts.cargar_datos import cargar_trabajadores
   cargar_trabajadores()

⚠️ Nota:
Ejecute este comando solo una vez. Si lo ejecuta más de una vez, los trabajadores se duplicarán en la base de datos.

Cómo Funciona la Votación
Validación del Votante:
Los votantes ingresan su número de documento para verificar que están habilitados para votar.

Registro del Voto:
Cada votante puede registrar su voto una sola vez.
Los votos se registran automáticamente en la base de datos.
Archivos Importantes
personal2024.xlsx: Archivo con la información del personal activo.
votacion/scripts/cargar_datos.py: Script para cargar los datos de los trabajadores en la base de datos.
Contribuciones
Cualquier sugerencia o mejora al sistema es bienvenida. Por favor, crea un pull request o abre un issue en este repositorio.



