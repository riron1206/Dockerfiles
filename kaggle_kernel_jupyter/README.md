# docker-compose.ymlでKaggle Kernel作成
- gcr.io/kaggle-images/python と kaggle_kernel_jupyter のイメージを作成して、kaggle_kernel_jupyterのコンテナを起動する
- docker-compose: Dockerfileのビルドと起動を管理するツール
	- docker-composeを使えば、様々なオプションをdocker-compose.ymlというYAMLファイルで設定することができる
	- docker-composeではイメージ名とコンテナ名を自動で生成される
- 参考: https://amalog.hateblo.jp/entry/data-analysis-docker

## 手順
- docker-compose.ymlの「C:\xxxx\kaggle_kernel_jupyter」を<docker-compose.yml置いているディレクトリ>の絶対パスに変更する
	- これをしないとディレクトリがマウントされない。$PWD でいけるはずだがなぜかエラーになる
- powershellで以下のコマンドを叩くとDockerfileのビルド（docker-compose.ymlをロードしてDockerfileでイメージ作成およびコンテナ起動。イメージ作成済みならコンテナ起動だけ）が走り、その後コンテナの中でJupyter Notebookが起動
```bash
$ cd <docker-compose.yml置いているディレクトリ>
$ docker-compose up --build  # up でコンテナを作成して、起動。--buildをつけることで起動前にイメージも構築

実行ログの「to login with a token:」の下のURLに表示されるtokenをつかって
http://localhost:8888/?token==xxxxxxxxxxxxxx  をブラウザのURLバーに入れればJupyter Notebookにアクセスできる

$ Ctrl + c でコンテナ停止
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)