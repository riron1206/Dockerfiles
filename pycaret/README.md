# pycaret���쐬
- pycaret: scikit-learn�AXGBoost�AMicrosoft LightGBM�AspaCy�ȂǁA�������̋@�B�w�K���C�u�����ƃt���[�����[�N��Python���b�p�[
- pycaret�Q�l: https://techtech-sorae.com/%e6%a9%9f%e6%a2%b0%e5%ad%a6%e7%bf%92%e3%81%ae%e8%87%aa%e5%8b%95%e5%8c%96%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa%e3%80%8cpycaret%e3%80%8d%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/
- VirturalBox�̃�����8G�ɕύX���邱��
	- �Q�l: https://qiita.com/niisan-tokyo/items/2d7d21aeb4e25f7a7bbe
- VirturalBox��port=8888�J���邱��
	- �Q�l: https://qiita.com/daijinload/items/85f6e84926f41812ed70

### Dockerfile�iOS �̃R�}���h�𗅗񂵂��e�L�X�g�t�@�C���j����docker�C���[�W�쐬���ăR���e�i�N���BDocker Quickstart Terminal�Ŏ��s
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/pycaret  # <Dockerfile�̊i�[�ꏊ>
$ docker build -t anarinsk/pycaret_jupyterlab:1.0.0 -f Dockerfile .
$ docker run -p 8888:8888 -it -m 8g -v $PWD:/pycaret --rm --entrypoint /bin/bash --name pycaret_jupyterlab anarinsk/pycaret_jupyterlab:1.0.0 # �R���e�i�N������bash�œ���
$ jupyter notebook --ip=0.0.0.0 --allow-root --NotebookApp.token=''  # jupyter notebook�N��
$ jupyter lab --ip=0.0.0.0 --allow-root --LabApp.token=''  # jupyter lab�N��

-p:�|�[�g�w��Bjupyter�g���ꍇ�K���K�v
-it:�^�[�~�i�����g�����߂̃I�v�V����
-m:�������w��
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