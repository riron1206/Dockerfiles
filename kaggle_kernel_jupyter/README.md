# kaggle_kernel_jupyter
docker-compose.yml���g�p���āAKaggle Kernel���\�z
- gcr.io/kaggle-images/python �� kaggle_kernel_jupyter �̃C���[�W���쐬���āAkaggle_kernel_jupyter�̃R���e�i���N��
- docker-compose�ł̓C���[�W���ƃR���e�i���������Ő��������
- �Q�l:https://amalog.hateblo.jp/entry/data-analysis-docker

## �菇
- docker-compose.yml�́uC:\xxxx\kaggle_kernel_jupyter�v��<docker-compose.yml�u���Ă���f�B���N�g��>�̐�΃p�X�ɕύX����
-- ��������Ȃ��ƃf�B���N�g�����}�E���g����Ȃ��B$PWD �ł�����͂������Ȃ����G���[�ɂȂ�
- powershell�ňȉ��̃R�}���h��@����Dockerfile�̃r���h�idocker-compose.yml�����[�h����Dockerfile�ŃC���[�W�쐬����уR���e�i�N���B�C���[�W�쐬�ς݂Ȃ�R���e�i�N�������j������A���̌�R���e�i�̒���Jupyter Notebook���N��
```bash
$ cd <docker-compose.yml�u���Ă���f�B���N�g��>
$ docker-compose up --build     # up �ŃR���e�i���쐬���āA�N���B--build�����邱�ƂŋN���O�ɃC���[�W���\�z

���s���O�́uto login with a token:�v�̉���URL�ɕ\�������token��������
http://localhost:8888/?token==xxxxxxxxxxxxxx  ���u���E�U��URL�o�[�ɓ�����Jupyter Notebook�ɃA�N�Z�X�ł���

$ Ctrl + c �ŃR���e�i��~
```

### ���̑��g��������docker-compose�̃R�}���h
```bash
$ docker-compose version        # docker-compose�̃o�[�W������\��
$ cd <docker-compose.yml�u���Ă���f�B���N�g��>
$ docker-compose ps             # docker-compose�ŋN�������R���e�i�̈ꗗ��\��
$ docker-compose up             # docker-compose�ŃC���[�W����R���e�i���N���B-d���ăo�b�N�O���E���h�Ŏ��s�����jupyter��token�\������Ȃ��̂�-d�͂��Ȃ�����
$ docker-compose kill           # docker-compose�ŋN�����̃R���e�i��������~
$ docker-compose restart        # docker-compose�ŋN�����̃R���e�i���ċN��
$ docker-compose rm             # docker-compose�Œ�~���̃R���e�i���폜
```

### ���̑��g��������docker�̃R�}���h
```bash
$ docker images                 # docker�C���[�W�̈ꗗ�m�F
$ docker rmi [IMAGE_ID]         # docker�C���[�W�̍폜
$ docker ps                     # �N������docker�R���e�i�̈ꗗ��\���B�S�ẴR���e�i�m�F����ꍇ��-a����
$ docker stop [CONTAINER_ID]    # �N������docker�R���e�i�̒�~
$ docker rm [CONTAINER_ID]      # �N������docker�R���e�i�̍폜 �����炩���ߒ�~���Ă�������
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)