#机器学习:分类学习
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()  # 花的数据
iris_X = iris.data  # 属性
iris_Y = iris.target  # 分类

##print(iris_X[:2, :])
##print(iris_Y)

X_train, X_test, Y_train, Y_test = train_test_split(  # 数据集分成训练集和测试集
    iris_X, iris_Y, test_size=0.3
)

##print(Y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)  # 自动完成学习的过程
print(knn.predict(X_test))
print(Y_test)