call C:\Users\<user>\Miniconda3\Scripts\activate.bat
call activate detection

rem # GPU�g����ꍇ�i�摜1�����_����̂�3�b���x������j
rem python ./model/FastRCNN_resnet152_inference.py -i ./test_images -o ./output -m C:test_env_restruct/model/FastRCNN_resnet152_ex002 --is_not_put_text

rem # CPU�Ŏ��s����ꍇ�i�摜1�����_����̂�40�b���x������j
python ./model/FastRCNN_resnet152_inference.py -i ./test_images -o ./output -m C:\test_env_restruct/model/FastRCNN_resnet152_ex002 --is_not_put_text -d cpu
