from kafka import KafkaConsumer
import json

class SocialMediaConsumer:
    def __init__(self, topic, bootstrap_servers="localhost:9092"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

    def consume_messages(self):
        for message in self.consumer:
            print("Received Tweet:", message.value)

if __name__ == "__main__":
    consumer = SocialMediaConsumer("social_media_stream")
    consumer.consume_messages()
