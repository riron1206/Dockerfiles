# pytorchの物体検出モデル推論環境作成例
```bash
$ 00_docker_build.sh    # docker imageビルド
$ 01_docker_run_cpu.sh  # cpuで推論実行。推論完了したらコンテナ閉じる
$ 01_docker_run_gpu.sh  # gpuで推論実行。推論完了したらコンテナ閉じる
```
batファイルから実行する例
```bash
run_inference.bat
```