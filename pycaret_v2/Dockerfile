FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y libgomp1
RUN apt-get update && apt-get install -y procps

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

CMD pytest