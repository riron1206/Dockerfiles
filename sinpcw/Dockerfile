FROM sinpcw/pytorch:1.7.1

RUN pip install -U pip && \
    pip install jupyterlab && \
    pip install jupyter-contrib-nbextensions && \
    pip install ipywidgets && \
    pip install papermill && \
    pip install pytorch-lightning

# JupyterNotebookの拡張機能を有効化（入力補完, 変数のハイライト機能, 目次）
RUN jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    jupyter nbextension enable highlight_selected_word/main &&\
    jupyter nbextension enable hinterland/hinterland && \
    jupyter nbextension enable toc2/main

WORKDIR /work