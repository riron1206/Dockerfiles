# pycaret���쐬
- pycaret: scikit-learn�AXGBoost�AMicrosoft LightGBM�AspaCy�ȂǁA�������̋@�B�w�K���C�u�����ƃt���[�����[�N��Python���b�p�[
- pycaret�Q�l: https://techtech-sorae.com/%e6%a9%9f%e6%a2%b0%e5%ad%a6%e7%bf%92%e3%81%ae%e8%87%aa%e5%8b%95%e5%8c%96%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa%e3%80%8cpycaret%e3%80%8d%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/

### Dockerfile�iOS �̃R�}���h�𗅗񂵂��e�L�X�g�t�@�C���j����docker�C���[�W�쐬���ăR���e�i�N���Bpowershell�Ŏ��s
```bash
$ cd <Dockerfile�̊i�[�ꏊ>
$ docker build -t anarinsk/pycaret_jupyterlab:1.0.0 -f Dockerfile .
$ docker run -p 8888:8888 -it -v $PWD/notebook:/notebook --rm --entrypoint /bin/bash --name pycaret_jupyterlab anarinsk/pycaret_jupyterlab:1.0.0 # �R���e�i�N������bash�œ���
$ jupyter lab --ip=0.0.0.0 --allow-root --LabApp.token=''  # jupyter lab�N��

-p:�|�[�g�w��Bjupyter�g���ꍇ�K���K�v
-it:�^�[�~�i�����g�����߂̃I�v�V����
-v:�w��f�B���N�g�����}�E���g
--rm:�R���e�i���甲����ƃR���e�i�������ō폜����
--name:�R���e�i��
--entrypoint:�R���e�i�N�����̓����B���pycaret�C���[�W�ł���anarinsk/pycaret:1.0.0��entrypoint��python�Ȃ̂�bash�ɕύX

��http://localhost:8888/���u���E�U��URL�o�[�ɓ�����JupyterLab�ɃA�N�Z�X�ł���

$ exit �ŃR���e�i��~
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)