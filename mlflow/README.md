# MLflow環境作成
- 参考: https://github.com/mlflow/mlflow/tree/master/examples/docker

### Dockerfile（OS のコマンドを羅列したテキストファイル）からdockerイメージ作成してコンテナ起動。powershellで実行
```bash
$ cd <Dockerfileの格納場所>
$ docker build -t mlflow -f Dockerfile .  # Dockerfileからイメージ作成。mlflowがdockerイメージ名になる
$ docker run -p 5000:5000 -it -v $PWD/jupyter_notebook:/jupyter_notebook --rm mlflow /bin/bash  # イメージからコンテナを作成し、コンテナ起動してbashで操作

-p:ポート指定。ポート指定しないとmlflow ui使えない
-it:ターミナルを使うためのオプション
-v:指定ディレクトリをマウント
--rm:コンテナから抜けるとコンテナを自動で削除する

$ cd <mlruns(mlflowの実行結果ディレクトリ)があるディレクトリ>
$ mlflow ui --port 5000 --host 0.0.0.0  # Dockerでは--host 0.0.0.0が必要。docker run -p 5000:5000 としたので--port 5000 
→http://localhost:5000/ をブラウザのURLバーに入れればmlflow uiにアクセスできる

$ Ctrl + c でコンテナ停止
```

### etc
- $ docker-compose up --build でdocker-compose.ymlから実行する場合はvolumesとworking_dirを変更する必要がある
- Dockerから起動したmlflow uiはartifactに設定したファイルを表示できない。これはmeta.yamlのartifact_locationが絶対パスであるため

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)