# pytorch�̃��f�����_��label-studio�i�A�m�e�[�V�����c�[���j�N��������쐬��
```bash
# gpu��docker-compose���琄�_���s
$ docker-compose -f docker-compose.yml up
# cpu��docker-compose���琄�_���s
$ docker-compose -f docker-compose_cpu.yml up
# docker-compose�̃R���e�i�ƃC���[�W�폜
$ docker-compose -f docker-compose_cpu.yml down --rmi all
```
bat�t�@�C��������s�����
```bash
run_inference_cpu.bat
```