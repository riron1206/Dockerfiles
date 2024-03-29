# Dockerfiles

Dockerfiles and docker-compose.yml sample command

## 非常に良くまとめられたdockerの使い方ドキュメント

- https://zenn.dev/a1008u/books/6bf96a769bedb2be53ae

## Docker setup (Windows10)

- 参考: https://qiita.com/ksh-fthr/items/6b1242c010fac7395a45

## dockerコンテナ作成例

- dockerコマンドは必ずPowerShellから実行すること
- 参考: https://karaage.hatenadiary.jp/entry/2019/05/17/073000

## Rancher Desktopからインストールする場合（Windows10）

- ※Rancher Desktop: Kubernetesコンテナ管理ツール。無料で使えるDocker for Windowsの理解
- https://zenn.dev/rhene/articles/rancher-desktop-for-windows-with-wsl2

## Docker for Windowsからインストールする場合

- wsl 2 のubuntuダウンロード
- Docker Desktop for Windows をインストール
- 参考:
  - 全体の手順: https://qiita.com/poramal/items/11912b5533ec8e7dbaac
  - Dockerダウンロード後に必要な設定: https://qiita.com/mofumoffy223/items/4f749dc10bd56b72feb5

## Docker Toolboxからインストールする場合

- 参考: https://qiita.com/KIYS/items/8ac37f6757a6b7f84569
  - VirturalBoxのメモリ8Gに変更すること
    - 参考: https://qiita.com/niisan-tokyo/items/2d7d21aeb4e25f7a7bbe
  - VirturalBoxのport=8888開けること
    - 参考: https://qiita.com/daijinload/items/85f6e84926f41812ed70
  - VirtualBox 仮想ディスクのサイズを変更すること
    - disk.vmdkをdisk.vdiに変更参考: https://qiita.com/satoysan/items/1a8ec50fa9eef295ba58
    - パーティション変更参考: http://kabatin.hateblo.jp/entry/2016/02/25/190846

### TensorFlowのイメージをDocker Hubからダウンロードしてコンテナ立ち上げ

```bash
$ docker run -it -v $PWD/../..:/jupyter_notebook --rm --name tensorflow tensorflow/tensorflow

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

## [Dockerfileでdl4uの環境作成](/dl4us)

## [Dockerfileでjupyterlab環境作成](/jupyterlab)

## [Dockerfileでmlflow環境作成](/mlflow)

## [Dockerfileでdarts環境作成](/darts)

## [Dockerfileでcpu版AzureMLの環境作成](/azureml_cpu)

## [Dockerfileでkaggle_gpu環境作成](/kaggle_gpu)

## [Dockerfileでpytorch1.7.1_gpu環境作成](/sinpcw)

## [Dockerfileでnumpyro_RTX3090環境作成](/numpyro_RTX3090)

## [Dockerfileでmmdetectionv2140環境作成](/mmdetectionv2140)

## [Dockerfileで物体検出モデル推論環境作成](/pytorch_object_detection_inf)

## [DockerHubからpyspark環境作成](/pyspark)

## [DockerHubからpycaret環境作成](/pycaret)

## [DockerHubからpycaret_v2環境作成](/pycaret_v2)

## [docker-compose.ymlでMeCab環境作成](/mecab)

## [docker-compose.ymlでKaggle Kernel作成](/kaggle_kernel_jupyter)

## [docker-compose.ymlでpytorchのモデル推論とlabel-studio（アノテーションツール）起動する作成例](/pytorch_label_studio)

## よく使うdockerコマンド

```bash
$ docker images                         # dockerイメージの一覧確認
$ docker rmi [IMAGE_ID]                 # dockerイメージの削除
$ docker rmi $(docker images -f "dangling=true" -q)  # noneのdockerイメージの削除一括削除
$ docker ps                             # 起動中のdockerコンテナの一覧を表示。全てのコンテナ確認する場合は-aつける
$ docker exec -it [CONTAINER_ID] bash   # 起動中のdockerコンテナをbashで操作する
$ docker stop [CONTAINER_ID]            # 起動中のdockerコンテナの停止
$ docker rm [CONTAINER_ID]              # 起動中のdockerコンテナの削除 ※docker stop [CONTAINER_ID]でコンテナ停止しておくこと
$ docker rm $(docker ps -a -q)          # 起動中の全てのコンテナの削除 ※docker stop $(docker ps -a -q)で全コンテナ停止しておくこと
```

## よく使うdocker-composeのコマンド

- Compose V2 からは `docker-compose` コマンドが `docker compose` になっているので注意

```bash
$ docker-compose version        # docker-composeのバージョンを表示
$ cd <docker-compose.yml置いているディレクトリ>
$ docker-compose ps             # docker-composeで起動したコンテナの一覧を表示
$ docker-compose up             # docker-composeでイメージからコンテナを起動。-dつけてバックグラウンドで実行するとjupyterのtoken表示されないので-dはつけないこと
$ docker-compose kill           # docker-composeで起動中のコンテナを強制停止
$ docker-compose restart        # docker-composeで起動中のコンテナを再起動
$ docker-compose rm             # docker-composeで停止中のコンテナを削除
```

## docker hubにimage登録

```bash
# 1. Docker Hubにログイン
$ docker login

# 2. upする [IMAGE ID] 確認
$ docker images

# 3. Docker Hub登録用のリポジトリ名とタグを付けたDockerイメージを別に作成
# $ docker tag [IMAGE ID] [自分のDockerID]/[Dockerイメージ名]:[タグ]
$ docker tag *** anonamename/xxx:latest

# 4. Docker Hubに登録（push）
# $ docker push [自分のDockerID]/[Dockerイメージ名]:[タグ]
$ docker push anonamename/xxx:latest
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## 作成したdockerイメージを人に渡す方法

[Dockerで構築する機械学習環境【2024年版】](https://zenn.dev/mkj/articles/33befbaf38c693)

```bash
# ubuntu-testイメージを保存。test.tar.gzが作られる
$ docker save ubuntu-test | gzip > test.tar.gz

# test.tar.gzを使ってubuntu-testイメージを作成
$ docker load < test.tar.gz
```

## Author

- Github: [riron1206](https://github.com/riron1206)
