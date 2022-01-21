import torch

N, D_in, H, D_out = 64, 1000, 100, 10

x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
 )

loss_fn = torch.nn.MSELoss(reduction='sum')


# 使用optim包定义优化器(Optimizer)
# Optimizer将会为我们更新模型的权重;
# 这里我们使用Adam优化方法:基于一阶梯度来优化随机目标函数的算法;
# Adam构造函数的第一个参数告诉优化器应该更新哪些张量。
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for t in range(500):
    y_pred = model(x)

    loss = loss_fn(y_pred, y)
    print(t, loss.item())

    optimizer.zero_grad()

    loss.backward()

    # 调用Optimizer优化器中的step函数使它所有参数更新!!!!!!
    optimizer.step()