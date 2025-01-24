# Proyecto 7 - Análisis de Zuber, empresa de viajes compartidos de Chicago. 

## Descripción

Proyecto para encontrar patrones en la información disponible: comprender las preferencias de los pasajeros y el impacto de los factores externos en los viajes.

Descripción de los datos
Una base de datos con información sobre viajes en taxi en Chicago: revisar el documento "chicago_weather.py" y la carpeta de sql_scripts (de dichos scripts se hicieron los archivos csv):

tabla neighborhoods: datos sobre los barrios de la ciudad

name: nombre del barrio
neighborhood_id: código del barrio
tabla cabs: datos sobre los taxis

cab_id: código del vehículo
vehicle_id: ID técnico del vehículo
company_name: la empresa propietaria del vehículo
tabla trips: datos sobre los viajes

trip_id: código del viaje
cab_id: código del vehículo que opera el viaje
start_ts: fecha y hora del inicio del viaje (tiempo redondeado a la hora)
end_ts: fecha y hora de finalización del viaje (tiempo redondeado a la hora)
duration_seconds: duración del viaje en segundos
distance_miles: distancia del viaje en millas
pickup_location_id: código del barrio de recogida
dropoff_location_id: código del barrio de finalización
tabla weather_records: datos sobre el clima

record_id: código del registro meteorológico
ts: fecha y hora del registro (tiempo redondeado a la hora)
temperature: temperatura cuando se tomó el registro
description: breve descripción de las condiciones meteorológicas, por ejemplo, "lluvia ligera" o "nubes dispersas"

## Contenido del Notebook
- **Total de celdas:** 32
- **Celdas de markdown:** 19
- **Celdas de código:** 13

### Procesos de análisis

1. **Carga de datos:**
   - Lectura de datos desde archivos fuente.
2. **Descripción de los datos:**
   - Método info para obtener información general de los datos.
3. **Preprocesamiento de los datos:**
   - Limpieza de datos.
   - Análisis de valores nulos.
   - Análisis de valores duplicados.
   - Análisis de valores únicos.
   - Transformación de datos.
4. **Análisis de los datos:**
   - Análisis de la distribución de los datos.
   - Análisis de los viajes por barrio.
   - Análisis de los viajes por día de la semana.
   - Análisis de los viajes por hora del día.
   - Análisis de los viajes por duración.
   - Análisis de los viajes por distancia.
   - Análisis de los viajes por clima.
   - Análisis de los viajes por temperatura.
   - Análisis de los viajes por descripción del clima.
   - Análisis de los viajes por compañía de taxis. 
   - Análisis estadísticos (t de student).
5. **Visualización de los datos:**
   - Creación de gráficos para visualizar los datos.
6. **Conclusiones:**
   - Resumen de los hallazgos y conclusiones del análisis.

## Requisitos del sistema

Para ejecutar este notebook, necesitarás:
- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Ejecución
1. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   ```

2. Cambia al directorio del proyecto:
   ```bash
   cd <nombre-del-directorio>
   ```

3. Abre y ejecuta el notebook:
   ```bash
   jupyter notebook proyecto_7.ipynb
   ```

## Contribuciones
Si deseas contribuir:
1. Realiza un fork del repositorio.
2. Crea una rama para tus cambios:
   ```bash
   git checkout -b mejora-analisis
   ```
3. Envía un pull request explicando tus cambios.

## Licencia
Consulta el archivo `LICENSE` para más información sobre el uso y distribución de este proyecto.
