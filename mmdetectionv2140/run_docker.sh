#docker build -t pytorch180_mmdet -f pytorch180_mmdet.Dockerfile .
#docker run -p 8888:8888 -it -v $PWD/work:/work -v /media/syokoi/vol1:/volume --ipc=host --rm --gpus all pytorch180_mmdet /bin/bash
#docker build -t pytorch170_mmdet -f pytorch170_mmdet.Dockerfile .
#docker run -p 8888:8888 -it -v $PWD/work:/work -v /media/syokoi/vol1:/volume --ipc=host --rm --gpus all pytorch170_mmdet /bin/bash
docker build -t pytorch170 -f pytorch170.Dockerfile .
docker run -p 8888:8888 -it -v $PWD/work:/work -v /media/syokoi/vol1:/volume --ipc=host --rm --gpus all pytorch170 /bin/bash
cd ..
jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8888