# https://github.com/riron1206/docker_ml より

# イメージ作成
docker build -t pytorch171 -f Dockerfile .

# コンテナ起動してbashで入る
# --gpus allでgpuすべて有効化
docker run -p 8888:8888 -p 8502:8502 -it -v $PWD/work:/work --rm --gpus all pytorch171 /bin/bash

# jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8888