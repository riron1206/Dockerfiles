# Dockerfile��dl4u�̊��쐬
- dl4us program of Tokyo Univ. Matsuo Lab: https://weblab.t.u-tokyo.ac.jp/dl4us/

### Dockerfile�iOS �̃R�}���h�𗅗񂵂��e�L�X�g�t�@�C���j����docker�C���[�W�쐬���ăR���e�i�N���Bpowershell�Ŏ��s
```bash
$ cd <Dockerfile�̊i�[�ꏊ>
$ docker build -t karaage0703/dl4us -f Dockerfile .                                    # Dockerfile����C���[�W�쐬�Bkaraage0703/dl4us��docker�C���[�W���ɂȂ�
$ docker run -p 8888:8888 -it -v $PWD/jupyter_notebook:/jupyter_notebook--rm karaage0703/dl4us /bin/bash   # �C���[�W����R���e�i���쐬���A�R���e�i�N������bash�ő���

-p:�|�[�g�w��Bjupyter�g���ꍇ�K���K�v
-it:�^�[�~�i�����g�����߂̃I�v�V����
-v:�w��f�B���N�g�����}�E���g
--rm:�R���e�i���甲����ƃR���e�i�������ō폜����

$ exit or Ctrl + D                                               # �R���e�i�̏I��
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)