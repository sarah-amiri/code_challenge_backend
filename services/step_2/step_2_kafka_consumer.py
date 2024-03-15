from connection import RedisConnection
from handlers import KafkaConsumerHandler

consumer = KafkaConsumerHandler()
redis = RedisConnection()


def consume_messages():
    for message in consumer.consume():
        redis.push_data(key=message['stock'], time=message['time'], price=int(message['price']))


if __name__ == '__main__':
    consume_messages()
