# pycaret_v2���쐬
- pycaret: scikit-learn�AXGBoost�AMicrosoft LightGBM�AspaCy�ȂǁA�������̋@�B�w�K���C�u�����ƃt���[�����[�N��Python���b�p�[
	- v2.0�ɂȂ蕪�ނł̃f�[�^�s�ύt�␳��mlflow�Ƃ̘A�g���ł���悤�ɂȂ���
	- pycaret v2.0�Q�l: https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104
- VirturalBox�̐ݒ�
	- VirturalBox�̃�����8G�ɕύX���邱��
		- �Q�l: https://qiita.com/niisan-tokyo/items/2d7d21aeb4e25f7a7bbe
	- VirturalBox��port=8888, 5000�J���邱�Ɓijupyter��mlflow ui�Ŏg���j
		- VirturalBox���ݒ聨�l�b�g���[�N�����x���|�[�g�t�H���[�f�B���O
		- �Q�l: https://qiita.com/daijinload/items/85f6e84926f41812ed70
- Docker Quickstart Terminal�Ŏ��s����

### Dockerfile����Docker image�쐬�i���ł�Docker image����Ȃ�s�v�j
- `requirements.txt`��pip�Œǉ�������python�p�b�P�[�W�����Ƃ��΋N�����ɃC���X�g�[������
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/pycaret_v2  # <Dockerfile�̊i�[�ꏊ>
$ docker build -t pycaret:2.0.0 -f Dockerfile .
```
### Docker�R���e�i�N��
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/pycaret_v2
$ docker run -p 8888:8888 -it -m 8g -v $PWD/../../..:/app --rm --entrypoint /bin/bash --name pycaret_v2 pycaret:2.0.0  # �R���e�i�N������bash�œ���
$ jupyter notebook --ip=0.0.0.0 --allow-root --NotebookApp.token=''  # jupyter notebook�N��

-p:�|�[�g�w��Bjupyter�g���ꍇ�K���K�v
-it:�^�[�~�i�����g�����߂̃I�v�V����
-m:�������w��
-v:�w��f�B���N�g�����}�E���g
--rm:�R���e�i���甲����ƃR���e�i�������ō폜����
--name:�R���e�i��
--entrypoint:�R���e�i�N�����̓����

��http://localhost:8888/���u���E�U��URL�o�[�ɓ�����Jupyter�ɃA�N�Z�X�ł���

$ exit or Ctrl+D �ŃR���e�i��~
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)