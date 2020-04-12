# pyspark環境作成
- 参考: https://yuku.takahashi.coffee/blog/2019/01/hello-pyspark

### DockerHubからdockerイメージコピーしてコンテナ起動。powershellで実行
```bash
$ docker pull jupyter/pyspark-notebook:87210526f381 # Jupyter Lab が公開している jupyter/pyspark-notebook
$ docker run --rm -w /app -p 8888:8888 --mount type=bind,src=$(pwd),dst=/app jupyter/pyspark-notebook:87210526f381 # コンテナ起動

--rm:コンテナから抜けるとコンテナを自動で削除する
-w:作業ディレクトリ
-p:ポート指定。ポート指定しないjupyter使えない
--mount:key=value形式でvolumeの指定してマウント。カレントディレクトリとマウントしている

→http://localhost:8888/?token==xxxxxxxxxxxxxx をブラウザのURLバーに入れればJupyter Notebookにアクセスできる

$ Ctrl + c でコンテナ停止
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)