# GPU使える場合（画像1枚推論するのに3秒程度かかる）
python ./model/FastRCNN_resnet152_inference.py -i ./test_images -o ./output -m $PWD/model/FastRCNN_resnet152_ex002 --is_not_put_text

# CPUで実行する場合（画像1枚推論するのに40秒程度かかる）
python ./model/FastRCNN_resnet152_inference.py -i ./test_images -o ./output -m $PWD/model/FastRCNN_resnet152_ex002 --is_not_put_text -d cpu
