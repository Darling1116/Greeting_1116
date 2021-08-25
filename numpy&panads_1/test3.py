import numpy as np
import pandas as pd

#concat:按行追加
'''
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
#print(df1)
#print(df2)
#print(df3)
res = pd.concat([df1, df2, df3], axis=1)
print(res)
res1 = pd.concat([df1, df2, df3], axis=1, ignore_index=True) # 索引重新排序
print(res1)
'''

'''
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'])
res = pd.concat([df1, df2])
print(res)

res1 = pd.concat([df1, df2], join='outer')
print(res1)

res2 = pd.concat([df1, df2], join='inner', ignore_index=True)
print(res2)
'''

#append：按列追加
'''
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])

res = df1.append(df2, ignore_index=True)
print(res)

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res1 = df1.append(s1, ignore_index=True)
print(res1)
'''

#merge合并
'''
left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'A': ['a0', 'a1', 'a2', 'a3'],
                     'B': ['b0', 'b1', 'b2', 'b3']})
right = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'C': ['c0', 'c1', 'c2', 'c3'],
                     'D': ['d0', 'd1', 'd2', 'd3']})
print(left)
print(right)
res = pd.merge(left, right, on='key')
#res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)
'''

'''
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
print(df2)

res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
'''

boys = pd.DataFrame({'k': ['k0', 'k1', 'k2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['k0', 'k0', 'k3'], 'age': [4, 5, 6]})
print(boys)
print(girls)

res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
res1 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')
print(res1)




