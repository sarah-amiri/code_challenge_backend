from kafka import KafkaConsumer, KafkaProducer
import json
import os
from typing import List


def serializer(message):
    return json.dumps(message).encode('utf-8')


class KafkaProducerHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self,
                 bootstrap_servers: List[str] = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', ['localhost:9092'])):
        self._producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                       value_serializer=serializer)

    def send(self, topic: str, message: str):
        self._producer.send(topic, message)



class KafkaConsumerHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self,
                 bootstrap_servers: List[str] = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', ['localhost:9092']),
                 topic_name: str = 'main_topic'):
        self._consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            # group_id='test_group',
            auto_offset_reset='earliest',
        )

    def consume(self):
        for message in self._consumer:
            yield json.loads(message.value)
