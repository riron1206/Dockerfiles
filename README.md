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

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)