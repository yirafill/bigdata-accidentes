# Proyecto Big Data - Análisis de Accidentes en Colombia

## Descripción del problema
Los accidentes de tránsito representan una problemática importante en Colombia debido a su impacto en la seguridad vial.

El objetivo de este proyecto es analizar un conjunto de datos de accidentes para identificar patrones como las zonas con mayor número de casos, utilizando herramientas de Big Data.

---

## Conjunto de datos

Se utilizó un dataset de datos abiertos de Colombia que contiene información sobre accidentes de tránsito.

Incluye variables como:
- Fecha del hecho
- Departamento
- Municipio
- Cantidad de accidentes

Fuente:
https://www.datos.gov.co/Transporte/Accidentalidad-Vial-en-Colombia/5xnn-7y9h

---

## Tecnologías utilizadas

- Apache Spark (procesamiento en batch)
- Apache Kafka (procesamiento en tiempo real)
- Python

---

## Procesamiento en batch (Spark)

Se desarrolló un script en Python llamado `batch_accidentes.py` que realiza:

- Carga del dataset
- Limpieza de datos
- Análisis exploratorio (EDA)
- Conteo de accidentes por departamento y municipio

---

## Procesamiento en tiempo real (Kafka y Spark Streaming)

Se implementó un sistema de streaming donde:

- `producer.py` simula la llegada de datos en tiempo real
- `consumer.py` consume los datos desde Kafka usando Spark Streaming

La comunicación se realiza en Putty, utilizando una ip en maquina virtual. 



