# Sistema de Votación al Trabajador del Año

![Captura2](https://github.com/user-attachments/assets/34447353-a8f2-4b99-a5b0-04498f4f3ba1)



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

## **Funcionamiento de la Votación**
### **Ingreso del Votante:**
- Los trabajadores ingresan su número de documento para verificar que están habilitados para votar.

### **Restricción de Voto Único:**
- El sistema permite registrar un voto por persona.

### **Registro Automático:**
- Los votos quedan registrados automáticamente en la base de datos, asegurando su integridad.

---

## **Estructura del Proyecto**
- **`personal2024.xlsx`:** Archivo que contiene la información de los trabajadores activos.
- **`votacion/scripts/cargar_datos.py`:** Script que carga los datos del personal desde el archivo Excel a la base de datos.

---

## **Notas Adicionales**
- Este sistema está diseñado para garantizar un proceso de votación transparente y eficiente.
- El personal elegible para votar y/o ser candidato se actualiza automáticamente al cargar los datos.





