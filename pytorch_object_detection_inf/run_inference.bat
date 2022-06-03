call C:\Users\<user>\Miniconda3\Scripts\activate.bat
call activate detection

rem # GPU使える場合（画像1枚推論するのに3秒程度かかる）
rem python ./model/FastRCNN_resnet152_inference.py -i ./test_images -o ./output -m C:test_env_restruct/model/FastRCNN_resnet152_ex002 --is_not_put_text

rem # CPUで実行する場合（画像1枚推論するのに40秒程度かかる）
python ./model/FastRCNN_resnet152_inference.py -i ./test_images -o ./output -m C:\test_env_restruct/model/FastRCNN_resnet152_ex002 --is_not_put_text -d cpu
