# Dockerfiles
Dockerfiles and docker-compose.yml sample command

## Docker setup (Windows10)
- �Q�l: https://qiita.com/ksh-fthr/items/6b1242c010fac7395a45

## docker�R���e�i�쐬��
- docker�R�}���h�͕K��PowerShell������s���邱��
- �Q�l: https://karaage.hatenadiary.jp/entry/2019/05/17/073000

### TensorFlow�̃C���[�W��Docker Hub����_�E�����[�h���ăR���e�i�����グ
```bash
$ docker run -it -v $PWD/docker_share:/share --rm --name tensorflow tensorflow/tensorflow

-it:�^�[�~�i�����g�����߂̃I�v�V����
-v $PWD/docker_share:/share : �z�X�g���ƃR���e�i���̃f�B���N�g�������L����I�v�V�����B�R�}���h���s�����f�B���N�g���̉��� docker_share �Ƃ����f�B���N�g������������A/share�f�B���N�g���Ƀt�@�C��������ƁA�z�X�g���ɂ����L�����
--rm:�R���e�i���甲����ƃR���e�i�������ō폜����
--name: �R���e�i�̖��O���w��
```

### Jupyter Notebook��������Docker Hub�̃C���[�W����R���e�i�����グ
```bash
$ docker run -p 8888:8888 -it --rm --name ds jupyter/datascience-notebook

-p:�|�[�g�w��Bjupyter�g���ꍇ�K���K�v

�N������Ɖ�ʂ� token=xxxxxxxxxxxxxx �Ƃ����`��token���\�������̂ŁAhttp://localhost:8888 �ɃA�N�Z�X���āA���O�C����ʂ�token�\��t����
�������́Ahttp://localhost:8888/?token=xxxxxxxxxxxxxx �ƃA�h���X��token��ł����߂΁A���O�C����ʂ��ȗ����Ē���Jupyter Notebook�Ƀ��O�C���ł���
```

## [Dockerfile��dl4u�̊��쐬](/dl4us)

## [Dockerfile��jupyterlab���쐬](/jupyterlab)

## [Dockerfile��mlflow���쐬](/mlflow)

## [DockerHub����pyspark���쐬](/pyspark)

## [DockerHub����pycaret���쐬](/pycaret)

## [docker-compose.yml��MeCab���쐬](/mecab)

## [docker-compose.yml��Kaggle Kernel�쐬](/kaggle_kernel_jupyter)

## �悭�g��docker�R�}���h
```bash
$ docker images                         # docker�C���[�W�̈ꗗ�m�F
$ docker rmi [IMAGE_ID]                 # docker�C���[�W�̍폜
$ docker ps                             # �N������docker�R���e�i�̈ꗗ��\���B�S�ẴR���e�i�m�F����ꍇ��-a����
$ docker exec -it [CONTAINER_ID] bash   # �N������docker�R���e�i��bash�ő��삷��
$ docker stop [CONTAINER_ID]            # �N������docker�R���e�i�̒�~
$ docker rm [CONTAINER_ID]              # �N������docker�R���e�i�̍폜 ��docker stop [CONTAINER_ID]�ŃR���e�i��~���Ă�������
$ docker rm $(docker ps -a -q)          # �N�����̑S�ẴR���e�i�̍폜 ��docker stop $(docker ps -a -q)�őS�R���e�i��~���Ă�������

```

## �悭�g��docker-compose�̃R�}���h
```bash
$ docker-compose version        # docker-compose�̃o�[�W������\��
$ cd <docker-compose.yml�u���Ă���f�B���N�g��>
$ docker-compose ps             # docker-compose�ŋN�������R���e�i�̈ꗗ��\��
$ docker-compose up             # docker-compose�ŃC���[�W����R���e�i���N���B-d���ăo�b�N�O���E���h�Ŏ��s�����jupyter��token�\������Ȃ��̂�-d�͂��Ȃ�����
$ docker-compose kill           # docker-compose�ŋN�����̃R���e�i��������~
$ docker-compose restart        # docker-compose�ŋN�����̃R���e�i���ċN��
$ docker-compose rm             # docker-compose�Œ�~���̃R���e�i���폜
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)