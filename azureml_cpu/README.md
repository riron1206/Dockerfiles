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



## azure ml のコマンド

### ※dockerファイル作ったが、azure ml のコマンドは基本的にはAzure上のnotebookでたたくみたい



#### Azure Machine Learning SDK でワークスペースに接続

- URL と パスワード が表示されて、そのURLにブラウザからアクセスし、パスワード入力したら認証完了
```python
$ python

from azureml.core import Workspace

ws = Workspace.get(name='ml_test',  # 接続する Azure ML ワークスペース名
                   subscription_id='779c53ba-06a7-4597-bec4-c1e64dac46b3',  # Azure サブスクリプションid
                   resource_group='ml_test'  # Azure リソースグループ名
                   )
```



#### Azure Machine Learning CLIでワークスペースに接続

- URL と パスワード が表示されて、そのURLにブラウザからアクセスし、パスワード入力したら認証完了
```bash
$ az login
```



#### Azure Machine Learning CLI 拡張機能でワークスペース内のコンピューティング先を一覧表示

- なぜかエラーになる...
- https://docs.microsoft.com/ja-jp/learn/modules/intro-to-azure-machine-learning-service/3-azure-ml-tools
```bash
$ az ml computetarget list -g 'aml-resources' -w 'aml-workspace'
```



#### jupyter 起動

```bash
$ jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8889

# http://localhost:8889/
```



## Author
- Github: [riron1206](https://github.com/riron1206)