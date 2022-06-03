import torch

TORCH_VERSION = ".".join(torch.__version__.split(".")[:2])
CUDA_VERSION = torch.__version__.split("+")[-1]
print("torch: ", TORCH_VERSION, "; cuda: ", CUDA_VERSION)

print("torch.cuda.is_available:", torch.cuda.is_available())

array = torch.zeros(4)  # 長さ4の配列を定義（これはcpu配列です）
print(array)
# 結果は tensor([0., 0., 0., 0.]) と表示されるはず

if torch.cuda.is_available():
    array_gpu = array.cuda()
    print(array_gpu)
    # 結果は tensor([0., 0., 0., 0.], device='cuda:0') と表示されるはず
