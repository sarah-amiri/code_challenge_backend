import csv
import os
import sys
from handlers import KafkaProducerHandler

file_name = 'price_data.csv'
producer = KafkaProducerHandler()
topic = 'main_topic'


def produce_messages():
    if not os.path.exists(file_name):
        sys.exit(1)
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            message = {
                'time': f'{row[0][:2]}:{row[0][2:4]}:{row[0][4:]}',
                'stock': row[1],
                'price': int(row[2]),
            }
            producer.send('main_topic', message)


if __name__ == '__main__':
    produce_messages()
