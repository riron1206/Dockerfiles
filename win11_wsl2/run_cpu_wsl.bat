@rem docker�f�[�����N��
wsl.exe sudo service docker start

@rem �����̃R���e�i���Əd�����Ă��܂����߃r���h�ł��Ȃ��̂ŃR���e�i����|
wsl.exe docker rm $(docker ps -aq) --force

wsl.exe docker-compose -f docker-compose.yml up model

pause