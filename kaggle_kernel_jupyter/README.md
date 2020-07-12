# docker-compose.ymlでKaggle Kernel作成
- gcr.io/kaggle-images/python と kaggle_kernel_jupyter のイメージを作成して、kaggle_kernel_jupyterのコンテナを起動する
- docker-compose: Dockerfileのビルドと起動を管理するツール
	- docker-composeを使えば、様々なオプションをdocker-compose.ymlというYAMLファイルで設定することができる
	- docker-composeではイメージ名とコンテナ名を自動で生成される
- 参考: https://amalog.hateblo.jp/entry/data-analysis-docker
- VirturalBoxのメモリ8Gに変更すること
	- 参考: https://qiita.com/niisan-tokyo/items/2d7d21aeb4e25f7a7bbe
- VirturalBoxのport=8888開けること
	- 参考: https://qiita.com/daijinload/items/85f6e84926f41812ed70
- VirtualBox 仮想ディスクのサイズを変更すること
	- disk.vmdkをdisk.vdiに変更参考: https://qiita.com/satoysan/items/1a8ec50fa9eef295ba58
	- パーティション変更参考: http://kabatin.hateblo.jp/entry/2016/02/25/190846

## 手順
- Docker Quickstart Terminalで以下のコマンドを叩くとDockerfileのビルド（docker-compose.ymlをロードしてDockerfileでイメージ作成およびコンテナ起動。イメージ作成済みならコンテナ起動だけ）が走り、その後コンテナの中でJupyter Notebookが起動
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/kaggle_kernel_jupyter  # <docker-compose.yml置いているディレクトリ>
$ docker-compose up --build  # up でコンテナを作成して、起動。--buildをつけることで起動前にイメージも構築
実行ログの「to login with a token:」の下のURLに表示されるtokenをつかって
http://localhost:8888/?token==xxxxxxxxxxxxxx  をブラウザのURLバーに入れればJupyter Notebookにアクセスできる
$ Ctrl + c でコンテナ停止

# bashで入る場合
$ docker run -p 8888:8888 -it -m 8g -v $PWD/notebook:/notebook --rm --entrypoint /bin/bash --name kaggle_kernel kaggle_kernel_jupyter_jupyter:latest # コンテナ起動してbashで入る
$ exit でコンテナ抜ける
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)