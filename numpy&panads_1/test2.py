import numpy as np
import pandas as pd

#数据筛选
'''
s = pd.Series([1, 3, 6, np.nan, 44, 1])
#print(s)

a = pd.DataFrame(np.arange(12).reshape((3, 4)))
#print(a)

dates = pd.date_range('20210101', periods=6)
#print(dates)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

print(df.A)  #print(df['A'])
print(df[0:3])

# 纯标签筛选
print(df.loc[:, ['A', 'B']])
#纯数字筛选
print(df.iloc[1, 1:3]) #第1行的第1到3位数（从0开始）

print(df[df.A > 8])
'''

#设置值
'''
dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[2, 2] = 1111
df.loc['20210101', 'B'] = 2222
df.B[df.A > 4] = 0
#df['F'] = np.nan
df.C[df.A == 20] = np.nan
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
print(df)
'''

#处理丢失数据

dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

print(df)
#print(df.dropna(axis=0, how='any'))
#print(df.isnull())

'''
#读取数据
data = pd.read_csv('student.csv')
#导出数据
data.to_pickle('student.csv')
'''