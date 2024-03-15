import csv
import os
import sys

from services.step_1.connection import RedisConnection

file_name = 'price_data.csv'
redis = RedisConnection()


def read_from_file():
    if not os.path.exists(file_name):
        sys.exit(1)
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')
        for index, row in enumerate(reader):
            if index > 0:
                yield row


def update_price():
    for row in read_from_file():
        time, key, price = row
        time = f'{time[:2]}:{time[2:4]}:{time[4:]}'
        redis.push_data(key, time, int(price))


if __name__ == '__main__':
    update_price()
