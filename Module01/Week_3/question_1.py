import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.exp(x)
        return x/sum(x)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.exp(x-max(x))
        return x/sum(x)

# Examples 1
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)
# >> tensor ([0.0900 , 0.2447 , 0.6652])

data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
# >> tensor ([0.0900 , 0.2447 , 0.6652])
