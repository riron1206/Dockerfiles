# MLflow���쐬
- �Q�l: https://github.com/mlflow/mlflow/tree/master/examples/docker

### Dockerfile�iOS �̃R�}���h�𗅗񂵂��e�L�X�g�t�@�C���j����docker�C���[�W�쐬���ăR���e�i�N���Bpowershell�Ŏ��s
```bash
$ cd <Dockerfile�̊i�[�ꏊ>
$ docker build -t mlflow-docker-example -f Dockerfile . # Dockerfile����C���[�W�쐬�Bmlflow-docker-example��docker�C���[�W���ɂȂ�
$ docker run -p 5000:5000 -it -v $PWD/jupyter_notebook:jupyter_notebook --rm mlflow-docker-example /bin/bash   # �C���[�W����R���e�i���쐬���A�R���e�i�N������bash�ő���

-p:�|�[�g�w��B�|�[�g�w�肵�Ȃ���mlflow ui�g���Ȃ�
-it:�^�[�~�i�����g�����߂̃I�v�V����
-v:�w��f�B���N�g�����}�E���g
--rm:�R���e�i���甲����ƃR���e�i�������ō폜����

$ cd <mlruns(mlflow�̎��s���ʃf�B���N�g��)������f�B���N�g��>
$ mlflow ui --port 5000 --host 0.0.0.0  # Docker�ł�--host 0.0.0.0���K�v�Bdocker run -p 5000:5000 �Ƃ����̂�--port 5000 
��http://localhost:5000/ ���u���E�U��URL�o�[�ɓ�����mlflow ui�ɃA�N�Z�X�ł���

$ Ctrl + c �ŃR���e�i��~
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)