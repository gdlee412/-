import pandas as pd
data_path='data/midterm_4.csv'

df = pd.read_csv(data_path)

category = input()

df = df[df['카테고리'] == category]
df = df[df['출금'] > 0]

df = df.sort_values(by = '출금', ascending = False)

out = pd.Series(df['출금'])
# 채점을 위한 코드입니다. out이 Series가 되도록 해주세요
print((out.iloc[0]),(out.iloc[-1]))