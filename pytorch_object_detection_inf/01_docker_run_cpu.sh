# Dockerコンテナ起動してbashで実行
docker run --name fastrcnn_resnet \
-it \
-v $PWD:/workspace \
-w /workspace \
--ipc=host \
--rm \
fastrcnn_resnet:1.0 \
/bin/bash run_inference.sh