## イメージ作成  sinpcw/pytorch:1.8.0 を使うとgpuのjaxは使えた
#docker build -t pytorch_numpyro_gpu -f pytorch18.Dockerfile .

# コンテナ起動してbashで入る
docker run -p 8888:8888 -p 8502:8502 -it -v $PWD/work:/work --rm --gpus all pytorch_numpyro_gpu /bin/bash

## gpu 確認
# python -c "import torch, jax, numpyro; print(torch.cuda.is_available()); print(jax.devices())"
## True
## [GpuDevice(id=0)]

## jax, numpyro動くか確認
## GPUだとMCMC遅いのでcpu使うこと
# python ./jax_numpyro_test.py

## jupyter 起動
# jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8888
## http://localhost:8888/lab?