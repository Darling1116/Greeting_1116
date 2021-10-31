#skleran的model:线性回归
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt  # 图像化


loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_y)

#print(model.predict(data_X[:4, :]))  # 输入x，预测y的值
#print(data_Y[:4])


#X, Y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)  # noise的大小可以控制离散程度
#plt.scatter(X, Y)
#plt.show()

print(model.coef_)  # 每个属性配套的参数
print(model.intercept_)  # 所对应的参数的值

print(model.get_params())  # 显示定义的参数
print(model.score(data_X, data_y))  # 显示预测的准确度