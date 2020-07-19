FROM anarinsk/pycaret:1.0.0

RUN apt update -y
RUN apt install git -y

RUN pip install -U pip && \
    pip install tqdm && \
    pip install jupyterlab && \
    pip install jupyter && \
    pip install papermill && \
    pip install git+https://github.com/pfnet-research/xfeat.git
