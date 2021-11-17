FROM sinpcw/pytorch:1.7.0

USER root

RUN apt-get update && apt-get install -y wget

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

# scikit-learnやseaborn入れる用
RUN pip install pycaret && \
    pip install xgboost && \
    pip install catboost && \
    pip install optuna

#RUN pip install effdet && \
#    pip install git+https://github.com/alexhock/object-detection-metrics && \
#    pip install ensemble-boxes

## pydot・graphvizをインストール(使わないからコメントアウト)
## https://qiita.com/dyokokawa6/items/2c42581fcbf1fa61ae46
#RUN pip install pydotplus
#RUN apt-get update -y
#RUN apt-get install -y graphviz
#RUN pip install graphviz


WORKDIR ./