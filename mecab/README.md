# docker-compose.yml��MeCab�i�`�ԑf��͂̃��C�u�����j���쐬
- MeCab+JupyterLab�̃R���e�i���N������
- docker-compose: Dockerfile�̃r���h�ƋN�����Ǘ�����c�[��
	- docker-compose���g���΁A�l�X�ȃI�v�V������docker-compose.yml�Ƃ���YAML�t�@�C���Őݒ肷�邱�Ƃ��ł���
	- docker-compose�ł̓C���[�W���ƃR���e�i���������Ő��������
- �Q�l: https://amalog.hateblo.jp/entry/data-analysis-docker

## �菇
- docker-compose.yml�́uC:\Users\shingo:�v��������PC�̐�΃p�X�ɕύX����
	- �������p�X�ɂ��Ȃ��ƃf�B���N�g�����}�E���g����Ȃ��B$PWD �ł�����͂������Ȃ����G���[�ɂȂ�
- powershell�ňȉ��̃R�}���h��@����Dockerfile�̃r���h�idocker-compose.yml�����[�h����Dockerfile�ŃC���[�W�쐬����уR���e�i�N���B�C���[�W�쐬�ς݂Ȃ�R���e�i�N�������j������A���̌�R���e�i�̒���Jupyter Notebook���N��
```bash
$ cd <docker-compose.yml�u���Ă���f�B���N�g��>
$ docker-compose up --build  # up �ŃR���e�i���쐬���āA�N���B--build�����邱�ƂŋN���O�ɃC���[�W���\�z

http://localhost:8888/  ���u���E�U��URL�o�[�ɓ�����JupyterLab�ɃA�N�Z�X�ł���

$ Ctrl + c �ŃR���e�i��~
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)