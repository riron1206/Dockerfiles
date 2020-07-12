# docker-compose.yml��Kaggle Kernel�쐬
- gcr.io/kaggle-images/python �� kaggle_kernel_jupyter �̃C���[�W���쐬���āAkaggle_kernel_jupyter�̃R���e�i���N������
- docker-compose: Dockerfile�̃r���h�ƋN�����Ǘ�����c�[��
	- docker-compose���g���΁A�l�X�ȃI�v�V������docker-compose.yml�Ƃ���YAML�t�@�C���Őݒ肷�邱�Ƃ��ł���
	- docker-compose�ł̓C���[�W���ƃR���e�i���������Ő��������
- �Q�l: https://amalog.hateblo.jp/entry/data-analysis-docker
- VirturalBox�̃�����8G�ɕύX���邱��
	- �Q�l: https://qiita.com/niisan-tokyo/items/2d7d21aeb4e25f7a7bbe
- VirturalBox��port=8888�J���邱��
	- �Q�l: https://qiita.com/daijinload/items/85f6e84926f41812ed70
- VirtualBox ���z�f�B�X�N�̃T�C�Y��ύX���邱��
	- disk.vmdk��disk.vdi�ɕύX�Q�l: https://qiita.com/satoysan/items/1a8ec50fa9eef295ba58
	- �p�[�e�B�V�����ύX�Q�l: http://kabatin.hateblo.jp/entry/2016/02/25/190846

## �菇
- Docker Quickstart Terminal�ňȉ��̃R�}���h��@����Dockerfile�̃r���h�idocker-compose.yml�����[�h����Dockerfile�ŃC���[�W�쐬����уR���e�i�N���B�C���[�W�쐬�ς݂Ȃ�R���e�i�N�������j������A���̌�R���e�i�̒���Jupyter Notebook���N��
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/kaggle_kernel_jupyter  # <docker-compose.yml�u���Ă���f�B���N�g��>
$ docker-compose up --build  # up �ŃR���e�i���쐬���āA�N���B--build�����邱�ƂŋN���O�ɃC���[�W���\�z
���s���O�́uto login with a token:�v�̉���URL�ɕ\�������token��������
http://localhost:8888/?token==xxxxxxxxxxxxxx  ���u���E�U��URL�o�[�ɓ�����Jupyter Notebook�ɃA�N�Z�X�ł���
$ Ctrl + c �ŃR���e�i��~

# bash�œ���ꍇ
$ docker run -p 8888:8888 -it -m 8g -v $PWD/notebook:/notebook --rm --entrypoint /bin/bash --name kaggle_kernel kaggle_kernel_jupyter_jupyter:latest # �R���e�i�N������bash�œ���
$ exit �ŃR���e�i������
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)