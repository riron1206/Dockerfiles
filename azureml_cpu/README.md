# AzureML���쐬
�Q�l: 

- https://hub.docker.com/_/microsoft-azureml
- https://docs.microsoft.com/ja-jp/python/api/overview/azure/ml/install?view=azure-ml-py



### Dockerfile����R���e�i�N���Bwsl2�Ŏ��s

```bash
$ docker build -t azureml_cpu -f Dockerfile .  # �C���[�W�쐬
$ docker run --rm -p 8889:8889 -it -v $PWD:$PWD azureml_cpu /bin/bash  # �R���e�i�N��

$ python -c "from azureml.core import Workspace"  # azureml �̃��C�u�����������m�F

--rm:�R���e�i���甲����ƃR���e�i�������ō폜����
-p:�|�[�g�w��B�|�[�g�w�肵�Ȃ�jupyter�g���Ȃ�
-it:�^�[�~�i�����g�����߂̃I�v�V����
-v:�w��f�B���N�g�����}�E���g

$ exit �ŃR���e�i����o��
```



## azure ml �̃R�}���h

### ��docker�t�@�C����������Aazure ml �̃R�}���h�͊�{�I�ɂ�Azure���notebook�ł������݂���



#### Azure Machine Learning SDK �Ń��[�N�X�y�[�X�ɐڑ�

- URL �� �p�X���[�h ���\������āA����URL�Ƀu���E�U����A�N�Z�X���A�p�X���[�h���͂�����F�؊���
```python
$ python

from azureml.core import Workspace

ws = Workspace.get(name='ml_test',  # �ڑ����� Azure ML ���[�N�X�y�[�X��
                   subscription_id='779c53ba-06a7-4597-bec4-c1e64dac46b3',  # Azure �T�u�X�N���v�V����id
                   resource_group='ml_test'  # Azure ���\�[�X�O���[�v��
                   )
```



#### Azure Machine Learning CLI�Ń��[�N�X�y�[�X�ɐڑ�

- URL �� �p�X���[�h ���\������āA����URL�Ƀu���E�U����A�N�Z�X���A�p�X���[�h���͂�����F�؊���
```bash
$ az login
```



#### Azure Machine Learning CLI �g���@�\�Ń��[�N�X�y�[�X���̃R���s���[�e�B���O����ꗗ�\��

- �Ȃ����G���[�ɂȂ�...
- https://docs.microsoft.com/ja-jp/learn/modules/intro-to-azure-machine-learning-service/3-azure-ml-tools
```bash
$ az ml computetarget list -g 'aml-resources' -w 'aml-workspace'
```



#### jupyter �N��

```bash
$ jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8889

# http://localhost:8889/
```



## Author
- Github: [riron1206](https://github.com/riron1206)