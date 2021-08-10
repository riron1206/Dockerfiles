# CUDA_VERSION=11.1.1 にする
# RTX3070以上のGPUはAmpere世代という新しいタイプらしい
# Ampere世代はCUDA=11.1でないと、tensorflow2.4.0がエラーになるらしい. 実際、CUDA=11.0の kaggle_gpu_image ではgpuのjaxがエラーになる
# https://qiita.com/masamiic/items/bb2cc8f0f4d7bf68b520
FROM sinpcw/pytorch:1.8.0

USER root

RUN pip install -U pip && \
    pip install jupyterlab && \
    pip install jupyter-contrib-nbextensions && \
    pip install ipywidgets && \
    pip install papermill && \
    pip install pytorch-lightning==1.3.8

# JupyterNotebookの拡張機能を有効化（入力補完, 変数のハイライト機能, 目次）
RUN jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    jupyter nbextension enable highlight_selected_word/main &&\
    jupyter nbextension enable hinterland/hinterland && \
    jupyter nbextension enable toc2/main

# https://github.com/google/jax
RUN pip install --upgrade pip
RUN pip install --upgrade "jax[cuda111]" -f https://storage.googleapis.com/jax-releases/jax_releases.html

# pip install -q ならgpu認識してくれる
# https://forum.pyro.ai/t/gpu-on-colab/2155/7
RUN pip install -q numpyro@git+https://github.com/pyro-ppl/numpyro && \
    pip install arviz

RUN pip install pyro-ppl

# scikit-learnやseaborn入れる用
RUN pip install tensorflow-gpu==2.4.1 && \
    pip install pycaret==2.3.1

# pydot・graphvizをインストール
# https://qiita.com/dyokokawa6/items/2c42581fcbf1fa61ae46
RUN pip install pydotplus
RUN apt-get update -y
RUN apt-get install -y graphviz
RUN pip install graphviz


WORKDIR /work