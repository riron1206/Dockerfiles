# for CPU
FROM mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04

# To avoid ImportError:ruamel.yaml
# https://docs.microsoft.com/ja-jp/python/api/overview/azure/ml/install?view=azure-ml-py
RUN conda install -c r -y conda python=3.6.2 pip=20.1.1

# Install pip dependencies. Please do not install azureml-sdk
# https://github.com/Azure/MachineLearningNotebooks/issues/1110
RUN pip install azureml-core && \
    pip install azureml-sdk azureml-widgets

# install Azure CLI
# https://docs.microsoft.com/ja-jp/cli/azure/install-azure-cli-linux?pivots=apt
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Add Azure Machine Learning CLI extension
# https://docs.microsoft.com/ja-jp/learn/modules/intro-to-azure-machine-learning-service/3-azure-ml-tools
RUN az extension add -n azure-cli-ml

# install other lib
RUN pip install pandas && \
    pip install matplotlib && \
    pip install mlflow && \
    pip install azureml-mlflow
