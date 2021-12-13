import torch

#requires_grad设为True，则会跟踪针对tensor的所有操作
x = torch.ones(2, 2, requires_grad=True)
print(x)

#grad_fn属性保存着创建了张量的Function引用(如果用户自己创建张量，则gard_fn是None)
y = x + 2
print(y)
#y作为操作结果被创建，所以它有grad_fn
print(y.grad_fn)

z = y * y * 3
out = z.mean()  # 求张量z的平均值
print(z)
print(z.grad_fn)
print(out)
print(out.grad_fn)

#out此时只包含一个标量27，使用backward进行后向传播
#out=0.25*Σ3(x+2)^2
out.backward()
#求梯度 d(out)/dx = 1/4 * 6x = 1.5x
print(x.grad)



# a = torch.randn(2, 2)
# a = ((a * 3) / (a - 1))
# print(a.requires_grad)
#
# a.requires_grad_(True)
# print(a.requires_grad)
# b = (a * a).sum()
# print(b.grad_fn)
