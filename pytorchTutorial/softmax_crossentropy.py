import torch
import torch.nn as nn
import numpy as np

loss = nn.CrossEntropyLoss()

Y = torch.tensor([2, 0, 1])
# nsamples x nclasses = 1x3
Y_pred_good = torch.tensor([[0.1, 1.0, 2.1],[2.0, 1.0, 0.1],[0.1, 3.0, 0.1]])
Y_pred_bad = torch.tensor([[0.5, 2.0, 0.3],[0.1, 1.0, 2.1],[0.1, 3.0, 0.1]])

l1 = loss(Y_pred_good,Y)
l2 = loss(Y_pred_bad,Y)
print(l1.item(), l2.item())

_, predictions1 = torch.max(Y_pred_good, 1)
_, predictions2 = torch.max(Y_pred_bad, 1)

print(predictions1,predictions2)



# # softmax: e^x/SUM_i e^(x_i)
# def softmax(x):
#     return np.exp(x)/np.sum(np.exp(x), axis=0)

# x = np.array([2.0, 1.0, 0.1])
# outputs = softmax(x)
# print('softmax numpy:', outputs)

# x = torch.tensor([2.0, 1.0, 0.1])
# outputs = torch.softmax(x, dim=0)
# print('tensor:', outputs)

# def cross_entropy(actual, predicted):
#     loss = -np.sum(actual * np.log(predicted))
#     return loss

# Y = np.array([1,0,0])

# Y_pred_good = np.array([0.7, 0.2, 0.1])
# Y_pred_bad = np.array([0.1, 0.3, 0.6])
# l1 = cross_entropy(Y, Y_pred_bad)
# l2 = cross_entropy(Y, Y_pred_good)

# print(l1, l2)