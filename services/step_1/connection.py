from collections import defaultdict
import json
import os
import redis


class RedisConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self,
                 host: str = os.getenv('REDIS_HOST', 'localhost'),
                 port: int = os.getenv('REDIS_PORT', 6379),
                 db: int = os.getenv('REDIS_DB', 0)):
        self.redis = redis.Redis(host=host, port=port, db=db)

    def push_data(self, key: str, time: str, price: int):
        data = self.redis.get(key)
        data = json.loads(data) if data is not None else defaultdict(list)
        data['time'].append(time)
        data['price'].append(price)
        self.redis.set(key, json.dumps(data))
