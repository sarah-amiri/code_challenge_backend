FROM python:3:11

WORKDIR /src

COPY . /src/step_1

RUN pip install redis

CMD ["python", "step_1_redis.py"]
