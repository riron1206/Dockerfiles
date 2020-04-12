# pyspark���쐬
- �Q�l: https://yuku.takahashi.coffee/blog/2019/01/hello-pyspark

### DockerHub����docker�C���[�W�R�s�[���ăR���e�i�N���Bpowershell�Ŏ��s
```bash
$ docker pull jupyter/pyspark-notebook:87210526f381 # Jupyter Lab �����J���Ă��� jupyter/pyspark-notebook
$ docker run --rm -w /app -p 8888:8888 --mount type=bind,src=$(pwd),dst=/app jupyter/pyspark-notebook:87210526f381 # �R���e�i�N��

--rm:�R���e�i���甲����ƃR���e�i�������ō폜����
-w:��ƃf�B���N�g��
-p:�|�[�g�w��B�|�[�g�w�肵�Ȃ�jupyter�g���Ȃ�
--mount:key=value�`����volume�̎w�肵�ă}�E���g�B�J�����g�f�B���N�g���ƃ}�E���g���Ă���

��http://localhost:8888/?token==xxxxxxxxxxxxxx ���u���E�U��URL�o�[�ɓ�����Jupyter Notebook�ɃA�N�Z�X�ł���

$ Ctrl + c �ŃR���e�i��~
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)