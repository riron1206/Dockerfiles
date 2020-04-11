# Dockerfileでdl4uの環境作成
- dl4us program of Tokyo Univ. Matsuo Lab: https://weblab.t.u-tokyo.ac.jp/dl4us/

### Dockerfile（OS のコマンドを羅列したテキストファイル）からdockerイメージ作成してコンテナ起動。powershellで実行
```bash
$ cd <Dockerfileの格納場所>
$ docker build -t karaage0703/dl4us -f Dockerfile .                                    # Dockerfileからイメージ作成。karaage0703/dl4usがdockerイメージ名になる
$ docker run -p 8888:8888 -it -v $PWD/jupyter_notebook:/jupyter_notebook--rm karaage0703/dl4us /bin/bash   # イメージからコンテナを作成し、コンテナ起動してbashで操作

-p:ポート指定。jupyter使う場合必ず必要
-it:ターミナルを使うためのオプション
-v:指定ディレクトリをマウント
--rm:コンテナから抜けるとコンテナを自動で削除する

$ exit or Ctrl + D                                               # コンテナの終了
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)