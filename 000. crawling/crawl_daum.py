# -*- coding: cp949 -*-
import pandas as pd

url = "http://realestate.daum.net/iframe/maemul/maemulList.daum?areaCode=2130010&mcateCode=A1&saleTypeCode=S&tabName=maemulList&isExpanded=false&page=1"
dfs = pd.read_html(url)

# 2���� DataFrame�� �о���

len(dfs)

df = dfs[1]
print(len(df), 'rows')

df.head(10)


df = df.dropna()
print(len(df), 'rows')

df.head(10)

# ix[] �ε����� ����Ͽ� ¦����° ��(row)�� �����Ѵ�.

df1 = df.ix[::2,:]

print(len(df1), 'rows')
df1.head(10)

# �̹����� Ȧ����° ��(row)�� �����Ѵ�.

df2 = df.ix[1::2, 0]
df2.name = '���'
df2.head(10)

# df1�� df2�� ��ġ��(concat)���� ���� index�� �����ϰ� �ʱ�ȭ �Ѵ�.
df1.reset_index(drop=True , inplace=True)
df2.reset_index(drop=True , inplace=True)

# df1 ��  df2 �� �÷����� ��ġ��
result = pd.concat([df1, df2], axis=1)
print(result.head(10))







