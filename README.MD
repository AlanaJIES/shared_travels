# Proyecto 7 - Análisis de Zuber, empresa de viajes compartidos de Chicago. 

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

## Requisitos
- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Ejecución
```bash
jupyter notebook proyecto_6.ipynb