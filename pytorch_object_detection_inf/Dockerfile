FROM sinpcw/pytorch:1.7.1

USER root

RUN apt-get update && apt-get install -y wget

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
