FROM python:3.6

RUN apt-get update \
  && apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig

RUN apt-get -y update && \
    apt-get -y install python-pip && \
    pip install mecab-python3 && \
    pip install natto-py && \
    pip install gensim && \
    pip install tqdm && \
    pip install jupyterlab
