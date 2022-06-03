FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime

USER root

RUN apt-get update && \
    apt-get install -y wget && \
    pip install -U pip && \
    pip install pillow==9.0.1 && \
    pip install opencv-python==4.5.5.62 && \
    pip install opencv-contrib-python==4.5.5.62 && \
    pip install tqdm==4.51.0 && \
    pip install scikit-learn==1.0.2 && \
    pip install pandas==1.4.0 && \
    pip install matplotlib==3.5.1 && \
    pip install numba==0.55.1

# 物体検出で使うもの
RUN pip install -U pip && \
    pip install ensemble-boxes==1.0.7 && \
    pip install albumentations==1.1.0

# 書き換え必要なもの
RUN pip install opencv-python-headless==4.5.4.58

# コンテナで作成したファイルをホスト側でも削除できるように一般ユーザー作成
ARG UID=1000
RUN useradd -m -u ${UID} docker
# 実行ユーザ指定
USER ${UID}

# 作業ディレクトリ指定
WORKDIR ./