# pycaret_v2環境作成
- pycaret: scikit-learn、XGBoost、Microsoft LightGBM、spaCyなど、いくつかの機械学習ライブラリとフレームワークのPythonラッパー
	- v2.0になり分類でのデータ不均衡補正やmlflowとの連携ができるようになった
	- pycaret v2.0参考: https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104
- VirturalBoxの設定
	- VirturalBoxのメモリ8Gに変更すること
		- 参考: https://qiita.com/niisan-tokyo/items/2d7d21aeb4e25f7a7bbe
	- VirturalBoxのport=8888, 5000開けること（jupyterとmlflow uiで使う）
		- VirturalBox→設定→ネットワーク→高度→ポートフォワーディング
		- 参考: https://qiita.com/daijinload/items/85f6e84926f41812ed70
- Docker Quickstart Terminalで実行する

### DockerfileからDocker image作成（すでにDocker imageあるなら不要）
- `requirements.txt`にpipで追加したいpythonパッケージ書いとけば起動時にインストールする
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/pycaret_v2  # <Dockerfileの格納場所>
$ docker build -t pycaret:2.0.0 -f Dockerfile .
```
### Dockerコンテナ起動
```bash
$ cd ../../Users/81908/jupyter_notebook/Dockerfiles/pycaret_v2
$ docker run -p 8888:8888 -it -m 8g -v $PWD/../../..:/app --rm --entrypoint /bin/bash --name pycaret_v2 pycaret:2.0.0  # コンテナ起動してbashで入る
$ jupyter notebook --ip=0.0.0.0 --allow-root --NotebookApp.token=''  # jupyter notebook起動

-p:ポート指定。jupyter使う場合必ず必要
-it:ターミナルを使うためのオプション
-m:メモリ指定
-v:指定ディレクトリをマウント
--rm:コンテナから抜けるとコンテナを自動で削除する
--name:コンテナ名
--entrypoint:コンテナ起動時の入り先

→http://localhost:8888/をブラウザのURLバーに入れればJupyterにアクセスできる

$ exit or Ctrl+D でコンテナ停止
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)