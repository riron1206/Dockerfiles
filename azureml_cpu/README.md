# AzureML環境作成
参考: 

- https://hub.docker.com/_/microsoft-azureml
- https://docs.microsoft.com/ja-jp/python/api/overview/azure/ml/install?view=azure-ml-py

### Dockerfileからコンテナ起動。wsl2で実行
```bash
$ docker build -t azureml_cpu -f Dockerfile .  # イメージ作成
$ docker run --rm -p 8889:8889 -it -v $PWD:$PWD azureml_cpu /bin/bash  # コンテナ起動

$ python -c "from azureml.core import Workspace"  # azureml のライブラリ動くか確認

--rm:コンテナから抜けるとコンテナを自動で削除する
-p:ポート指定。ポート指定しないjupyter使えない
-it:ターミナルを使うためのオプション
-v:指定ディレクトリをマウント

$ exit でコンテナから出る
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)