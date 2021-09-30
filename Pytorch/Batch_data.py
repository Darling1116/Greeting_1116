import torch
import torch.utils.data as Data

BATCH_SIZE = 5

x = torch.linspace(1, 10, 10)  # x为从1到10,10个点
y = torch.linspace(10, 1, 10)  # y为从10到1,10个点

torch_dataset = Data.TensorDataset(x, y)
loader = Data.DataLoader(
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0,  # 这里我把参数从2改成了0？？？
)

for epoch in range(3):  # 把数据整体训练3次
    for step, (batch_x, batch_y) in enumerate(loader):
        # training.....
        print('Epoch: ', epoch, '| step: ', step, '| batch x: ', batch_x.numpy(), '| batch y: ', batch_y.numpy())

