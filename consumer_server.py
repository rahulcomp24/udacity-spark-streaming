from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "service_calls",
    group_id="test",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
)
for msg in consumer:
    print(msg)
