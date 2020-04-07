# kaggle_kernel_jupyter
docker-compose.ymlを使用して、Kaggle Kernelを構築
- gcr.io/kaggle-images/python と kaggle_kernel_jupyter のイメージを作成して、kaggle_kernel_jupyterのコンテナを起動
- docker-composeではイメージ名とコンテナ名を自動で生成される
- 参考:https://amalog.hateblo.jp/entry/data-analysis-docker

## 手順
- docker-compose.ymlの「C:\xxxx\kaggle_kernel_jupyter」を<docker-compose.yml置いているディレクトリ>の絶対パスに変更する
-- これをしないとディレクトリがマウントされない。$PWD でいけるはずだがなぜかエラーになる
- powershellで以下のコマンドを叩くとDockerfileのビルド（docker-compose.ymlをロードしてDockerfileでイメージ作成およびコンテナ起動。イメージ作成済みならコンテナ起動だけ）が走り、その後コンテナの中でJupyter Notebookが起動
```bash
$ cd <docker-compose.yml置いているディレクトリ>
$ docker-compose up --build     # up でコンテナを作成して、起動。--buildをつけることで起動前にイメージも構築

実行ログの「to login with a token:」の下のURLに表示されるtokenをつかって
http://localhost:8888/?token==xxxxxxxxxxxxxx  をブラウザのURLバーに入れればJupyter Notebookにアクセスできる

$ Ctrl + c でコンテナ停止
```

### その他使いそうなdocker-composeのコマンド
```bash
$ docker-compose version        # docker-composeのバージョンを表示
$ cd <docker-compose.yml置いているディレクトリ>
$ docker-compose ps             # docker-composeで起動したコンテナの一覧を表示
$ docker-compose up             # docker-composeでイメージからコンテナを起動。-dつけてバックグラウンドで実行するとjupyterのtoken表示されないので-dはつけないこと
$ docker-compose kill           # docker-composeで起動中のコンテナを強制停止
$ docker-compose restart        # docker-composeで起動中のコンテナを再起動
$ docker-compose rm             # docker-composeで停止中のコンテナを削除
```

### その他使いそうなdockerのコマンド
```bash
$ docker images                 # dockerイメージの一覧確認
$ docker rmi [IMAGE_ID]         # dockerイメージの削除
$ docker ps                     # 起動中のdockerコンテナの一覧を表示。全てのコンテナ確認する場合は-aつける
$ docker stop [CONTAINER_ID]    # 起動中のdockerコンテナの停止
$ docker rm [CONTAINER_ID]      # 起動中のdockerコンテナの削除 ※あらかじめ停止しておくこと
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)