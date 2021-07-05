# イメージ作成  kaggle_gpu を使うがgpuのjaxは使えない
docker build -t kaggle_numpyro -f Dockerfile .

# コンテナ起動してbashで入る
docker run -p 8888:8888 -p 8502:8502 -it -v $PWD/work:/work --rm --gpus all kaggle_numpyro /bin/bash

## gpu 確認
# python -c "import torch, jax, numpyro; print(torch.cuda.is_available()); print(jax.devices())"
## True
## [CpuDevice(id=0)]  # jaxはcpuしか認識できない

## jax, numpyro動くか確認
# python ./jax_numpyro_test.py

## jupyter 起動
# jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8888
## http://localhost:8888/lab?