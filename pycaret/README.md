# pycaret環境作成
- pycaret: scikit-learn、XGBoost、Microsoft LightGBM、spaCyなど、いくつかの機械学習ライブラリとフレームワークのPythonラッパー
- pycaret参考: https://techtech-sorae.com/%e6%a9%9f%e6%a2%b0%e5%ad%a6%e7%bf%92%e3%81%ae%e8%87%aa%e5%8b%95%e5%8c%96%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa%e3%80%8cpycaret%e3%80%8d%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/

### Dockerfile（OS のコマンドを羅列したテキストファイル）からdockerイメージ作成してコンテナ起動。powershellで実行
```bash
$ cd <Dockerfileの格納場所>
$ docker build -t anarinsk/pycaret_jupyterlab:1.0.0 -f Dockerfile .
$ docker run -p 8888:8888 -it -v $PWD/notebook:/notebook --rm --entrypoint /bin/bash --name pycaret_jupyterlab anarinsk/pycaret_jupyterlab:1.0.0 # コンテナ起動してbashで入る
$ jupyter lab --ip=0.0.0.0 --allow-root --LabApp.token=''  # jupyter lab起動

-p:ポート指定。jupyter使う場合必ず必要
-it:ターミナルを使うためのオプション
-v:指定ディレクトリをマウント
--rm:コンテナから抜けるとコンテナを自動で削除する
--name:コンテナ名
--entrypoint:コンテナ起動時の入り先。野良pycaretイメージであるanarinsk/pycaret:1.0.0はentrypointがpythonなのでbashに変更

→http://localhost:8888/をブラウザのURLバーに入れればJupyterLabにアクセスできる

$ exit でコンテナ停止
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)