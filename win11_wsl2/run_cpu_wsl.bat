@rem dockerデーモン起動
wsl.exe sudo service docker start

@rem 既存のコンテナ名と重複してしまうためビルドできないのでコンテナを一掃
wsl.exe docker rm $(docker ps -aq) --force

wsl.exe docker-compose -f docker-compose.yml up model

pause