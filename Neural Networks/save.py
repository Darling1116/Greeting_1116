from sklearn import svm
from sklearn import datasets
import pickle
import joblib

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

'''
#save method 1:pickle
#打开并保存数据到clf.pickle
with open('D:/Workspaces/save/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)

#读取数据
with open('D:/Workspaces/save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))
'''

#save method 2:joblib
#save
joblib.dump(clf, 'D:/Workspaces/save/clf.pkl')

#restore
clf3 = joblib.load('D:/Workspaces/save/clf.pkl')
print(clf3.predict(X[0:1]))