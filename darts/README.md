# darts環境作成
- 参考: https://pypi.org/project/u8darts/
- Darts: 時系列に関する様々なモデルを scikit-learn ベースのAPIで統一的に扱うことができるパッケージ

### とりあえず動かす方法
- poetry使ってpipでinstallするとpystanのinstallで死にます
- 以下のコマンドでもfbprophet のインストールでエラーメッセージ出るがなぜか動く
```bash
$ cd C:\Users\81908\Git
$ git clone https://github.com/unit8co/darts.git  # gitインストール必要
$ cd darts
$ cd scripts ./build_docker.sh && ./run_docker.sh

$ Ctrl + c でコンテナ停止
```

<!-- 
## License
This software is released under the MIT License, see LICENSE.
-->

## Author
- Github: [riron1206](https://github.com/riron1206)