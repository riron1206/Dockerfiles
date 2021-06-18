# CPU版
FROM mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04

# To avoid ImportError:ruamel.yaml
# https://docs.microsoft.com/ja-jp/python/api/overview/azure/ml/install?view=azure-ml-py
RUN conda install -c r -y conda python=3.6.2 pip=20.1.1

# Install pip dependencies. Please do not install azureml-sdk
# https://github.com/Azure/MachineLearningNotebooks/issues/1110
RUN pip install azureml-core==1.30.0
