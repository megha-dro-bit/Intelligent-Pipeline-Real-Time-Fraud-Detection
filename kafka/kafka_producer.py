from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(20):
    transaction = {
        "amount": random.randint(100, 5000),
        "oldbalanceOrg": random.randint(1000, 10000),
        "newbalanceOrig": random.randint(0, 9000)
    }

    producer.send("fraud-transactions", transaction)
    print("Sent:", transaction)
    time.sleep(1)

producer.flush()
