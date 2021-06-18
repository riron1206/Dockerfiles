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

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)