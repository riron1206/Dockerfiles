FROM gcr.io/kaggle-gpu-images/python:v100

# cpu版はpipでinstallできる
RUN pip install -U pip && \
    pip install numpyro==0.6.0 && \
    pip install arviz

WORKDIR /work