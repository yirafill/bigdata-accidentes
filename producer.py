from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

departamentos = ["ATLANTICO", "ANTIOQUIA", "VALLE", "CUNDINAMARCA"]

while True:
    data = {
        "departamento": random.choice(departamentos),
        "accidentes": random.randint(1, 10)
    }

    producer.send('accidentes', value=data)
    print("Enviado:", data)
    time.sleep(2)
