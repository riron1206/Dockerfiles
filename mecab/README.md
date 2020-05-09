# docker-compose.ymlでMeCab（形態素解析のライブラリ）環境作成
- MeCab+JupyterLabのコンテナを起動する
- docker-compose: Dockerfileのビルドと起動を管理するツール
	- docker-composeを使えば、様々なオプションをdocker-compose.ymlというYAMLファイルで設定することができる
	- docker-composeではイメージ名とコンテナ名を自動で生成される
- 参考: https://amalog.hateblo.jp/entry/data-analysis-docker

## 手順
- docker-compose.ymlの「C:\Users\shingo:」を自分のPCの絶対パスに変更する
	- 正しいパスにしないとディレクトリがマウントされない。$PWD でいけるはずだがなぜかエラーになる
- powershellで以下のコマンドを叩くとDockerfileのビルド（docker-compose.ymlをロードしてDockerfileでイメージ作成およびコンテナ起動。イメージ作成済みならコンテナ起動だけ）が走り、その後コンテナの中でJupyter Notebookが起動
```bash
$ cd <docker-compose.yml置いているディレクトリ>
$ docker-compose up --build  # up でコンテナを作成して、起動。--buildをつけることで起動前にイメージも構築

http://localhost:8888/  をブラウザのURLバーに入れればJupyterLabにアクセスできる

$ Ctrl + c でコンテナ停止
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)