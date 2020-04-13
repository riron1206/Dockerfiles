# DockerfileでJupyter Lab環境作成
- https://datawokagaku.com/startjupyternote/

### Dockerfile（OS のコマンドを羅列したテキストファイル）からdockerイメージ作成してコンテナ起動。powershellで実行
```bash
$ cd <Dockerfileの格納場所>
$ docker build -t jupyterlab -f Dockerfile .  # Dockerfileからイメージ作成。jupyterlabがdockerイメージ名になる
$ docker run -p 8888:8888 -it -v $PWD/notebook:/notebook --rm --name jupyterlab jupyterlab  # イメージからコンテナを作成し、コンテナ起動してjupyterlab起動

-p:ポート指定。jupyter使う場合必ず必要
-it:ターミナルを使うためのオプション
-v:指定ディレクトリをマウント
--rm:コンテナから抜けるとコンテナを自動で削除する
--name:コンテナ名

$ exit or Ctrl + D                                               # コンテナの終了
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)