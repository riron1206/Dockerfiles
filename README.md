# Dockerfiles
Dockerfiles and docker-compose.yml sample command

## Docker setup (Windows10)
- 参考: https://qiita.com/ksh-fthr/items/6b1242c010fac7395a45

## dockerコンテナ作成例
- dockerコマンドは必ずPowerShellから実行すること
- 参考: https://karaage.hatenadiary.jp/entry/2019/05/17/073000

### TensorFlowのイメージをDocker Hubからダウンロードしてコンテナ立ち上げ
```bash
$ docker run -it -v $PWD/docker_share:/share --rm --name tensorflow tensorflow/tensorflow

-it:ターミナルを使うためのオプション
-v $PWD/docker_share:/share : ホスト側とコンテナ側のディレクトリを共有するオプション。コマンド実行したディレクトリの下に docker_share というディレクトリが生成され、/shareディレクトリにファイルを入れると、ホスト側にも共有される
--rm:コンテナから抜けるとコンテナを自動で削除する
--name: コンテナの名前を指定
```

### Jupyter Notebookが入ったDocker Hubのイメージからコンテナ立ち上げ
```bash
$ docker run -p 8888:8888 -it --rm --name ds jupyter/datascience-notebook

-p:ポート指定。jupyter使う場合必ず必要

起動すると画面に token=xxxxxxxxxxxxxx という形でtokenが表示されるので、http://localhost:8888 にアクセスして、ログイン画面でtoken貼り付ける
もしくは、http://localhost:8888/?token=xxxxxxxxxxxxxx とアドレスにtokenを打ち込めば、ログイン画面を省略して直接Jupyter Notebookにログインできる
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)