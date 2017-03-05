# -*- coding: cp949 -*-
import pandas as pd

url = "http://realestate.daum.net/iframe/maemul/maemulList.daum?areaCode=2130010&mcateCode=A1&saleTypeCode=S&tabName=maemulList&isExpanded=false&page=1"
dfs = pd.read_html(url)

# 2개의 DataFrame을 읽었다

len(dfs)

df = dfs[1]
print(len(df), 'rows')

df.head(10)


df = df.dropna()
print(len(df), 'rows')

df.head(10)

# ix[] 인덱싱을 사용하여 짝수번째 행(row)만 추출한다.

df1 = df.ix[::2,:]

print(len(df1), 'rows')
df1.head(10)

# 이번에는 홀수번째 행(row)만 추출한다.

df2 = df.ix[1::2, 0]
df2.name = '비고'
df2.head(10)

# df1과 df2를 합치기(concat)위해 위해 index를 동일하게 초기화 한다.
df1.reset_index(drop=True , inplace=True)
df2.reset_index(drop=True , inplace=True)

# df1 과  df2 를 컬럼으로 합치기
result = pd.concat([df1, df2], axis=1)
print(result.head(10))







