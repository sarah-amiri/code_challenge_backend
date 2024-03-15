FROM python:3:11

WORKDIR /src

COPY . /src/step_2

RUN pip install redis
RUN pip install kafka-python
RUN chmod a+x script.sh

CMD ["./script.sh"]
