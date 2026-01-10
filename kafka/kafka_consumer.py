from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "fraud-transactions",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for transactions...")

for message in consumer:
    print("Received transaction:", message.value)
    print("Fraud prediction: NOT FRAUD (demo)")
