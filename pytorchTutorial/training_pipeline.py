# 1) Design model (input, output size, forward pass)
# 2) Construct loss and optimizer
# 3) Training loop
#   - foward pass: compute prediction
#   - backward pass: gradients
#   - update weights
import torch
import torch.nn as nn

# f = w * x
# f = 2 * x

X = torch.tensor([[1],[2],[3],[4]],dtype=torch.float32)
Y = torch.tensor([[2],[4],[6],[8]],dtype=torch.float32)

X_test = torch.tensor([5],dtype = torch.float32)
n_samples, n_features = X.shape
print(n_samples, n_features)

input_size = n_features
output_size = n_features

# using the default nn Linear regression model:
#model = nn.Linear(input_size, output_size)

# make a class for the model:
class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression,self).__init__()

        self.lin = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.lin(x)

model = LinearRegression(input_size, output_size)


def gradient(x,y,y_predicted):
    return torch.dot(2*x,y_predicted-y).mean()


print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

learning_rate = 0.01
n_iters=1000

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

for epoch in range(n_iters):
    y_pred = model(X)

    l = loss(Y, y_pred)

    l.backward() # dl/dw

    optimizer.step()

    optimizer.zero_grad()

    if (epoch ) % 100  == 0:
        [w,b] = model.parameters()
        print(f'epoch {epoch+1}: w = {w[0][0].item():.3f}, loss = {l:.3f}')

print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')
