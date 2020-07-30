# Streamlit on Docker �̊ۃR�s�[
- https://github.com/MrTomerLevi/streamlit-docker
- ��Virtual Box�g���Ă�ꍇ��8501�|�[�g�J���Ƃ��K�v������i�ݒ聨�l�b�g���[�N�����x���|�[�g�t�H���[�f�B���O�j

# Streamlit: python�A�v�����t���[�����[�N
- �e�L�X�g�{�b�N�X��{�^�����삾���̊ȒP��WEB�A�v�����쐬���A���J�������Ƃ���A������Ƃ����Г��c�[����WEB�Ŏ����������Ƃ��Ɏg����
- �A�v���̌����ڂ̓R�[�h������Ȃ�jupyter
- python�ł�shiny�Ƃ����F���ł悳����
- �t�@�C���_�E�����[�h�⃍�O�C������͂ł��Ȃ��̂ł��̏ꍇ��Flask�g����
- Project docs: https://streamlit.io/docs/

<p align="center">
  <img src="img/streamlit.png" width="750" title="Example Streamlit App">
</p>

## Docker image��Docker Hub�̂�����: 
Pull
`docker pull tomerlevi/streamlit-docker`

*Page: https://cloud.docker.com/u/tomerlevi/repository/docker/tomerlevi/streamlit-docker

## Build ���@�i���ł�Docker image����Ȃ�s�v�j
- `requirements.txt`��pip�Œǉ�������python�p�b�P�[�W�����Ƃ��΋N�����ɃC���X�g�[������
```bash
Docker Quickstart Terminal�J����
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/streamlit/
$ docker build -t tomerlevi/streamlit-docker -f Dockerfile .  # Docker image�쐬����
```

## streamlit scrip t�̃T���v�����s
- �A�v���� http://localhost:8501 ���炢�����
- $ Ctrl + c �ŃR���e�i��~
```bash
$ docker run --rm -it -p 8501:8501 tomerlevi/streamlit-docker /examples/intro.py
$ docker run --rm -it -p 8501:8501 tomerlevi/streamlit-docker /examples/plot_example.py
$ docker run --rm -it -p 8501:8501 tomerlevi/streamlit-docker /examples/uber_nyc_data_explorer.py
```

## ���[�J��(src�f�B���N�g��)�� streamlit script ������
- �X�N���v�g�ҏW���ău���E�U�X�V����ƁA���ύX���f�����
```bash
$ docker run -p 8501:8501 -it -m 8g -v $PWD:/app --rm --entrypoint /bin/bash tomerlevi/streamlit-docker  # �R���e�i�N������bash�œ���
$ streamlit run src/intro.py
$ streamlit run src/my_test_coronavirus_trend.py
```

## GitHub�ɏオ���Ă��� streamlit script �����[�J���N���[�������Ŏ��s
- �Q�l: https://qiita.com/prs-watch/items/ca5589a725c479e8c489
```bash
$ docker run -p 8501:8501 -it -m 8g -v $PWD:/app --rm --entrypoint /bin/bash tomerlevi/streamlit-docker  # �R���e�i�N������bash�œ���
$ streamlit run https://raw.githubusercontent.com/prs-watch/streamlit-sample/master/sample.py
```
