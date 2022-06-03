# pytorchのモデル推論とlabel-studio（アノテーションツール）起動する環境作成例
```bash
# gpuでdocker-composeから推論実行
$ docker-compose -f docker-compose.yml up
# cpuでdocker-composeから推論実行
$ docker-compose -f docker-compose_cpu.yml up
# docker-composeのコンテナとイメージ削除
$ docker-compose -f docker-compose_cpu.yml down --rmi all
```
batファイルから実行する例
```bash
run_inference_cpu.bat
```