# Dockerfile��Jupyter Lab���쐬
- https://datawokagaku.com/startjupyternote/

### Dockerfile�iOS �̃R�}���h�𗅗񂵂��e�L�X�g�t�@�C���j����docker�C���[�W�쐬���ăR���e�i�N���Bpowershell�Ŏ��s
```bash
$ cd <Dockerfile�̊i�[�ꏊ>
$ docker build -t jupyterlab -f Dockerfile .  # Dockerfile����C���[�W�쐬�Bjupyterlab��docker�C���[�W���ɂȂ�
$ docker run -p 8888:8888 -it -v $PWD/notebook:/notebook --rm --name jupyterlab jupyterlab  # �C���[�W����R���e�i���쐬���A�R���e�i�N������jupyterlab�N��

-p:�|�[�g�w��Bjupyter�g���ꍇ�K���K�v
-it:�^�[�~�i�����g�����߂̃I�v�V����
-v:�w��f�B���N�g�����}�E���g
--rm:�R���e�i���甲����ƃR���e�i�������ō폜����
--name:�R���e�i��

$ exit or Ctrl + D                                               # �R���e�i�̏I��
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)