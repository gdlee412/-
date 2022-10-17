import pandas as pd

data_path='data/midterm_4.csv'

#read csv
df = pd.read_csv(data_path)

#remove 0출금 values
df = df[df['출금'] > 0]

#aggregate function
agg_function = {'일시': 'first', '입금':'sum', '출금':'sum', '잔고': 'sum'}

#groupby function while adding up the 출금
gb = df.groupby(df['카테고리']).aggregate(agg_function)

#sort into descending order
gb = gb.sort_values(by = '출금', ascending = False)

#create out using series
out = pd.Series(gb['출금'])
import numpy as np

# 채점용 코드입니다. out이 데이터프레임이 되도록 해주세요.
# out 데이터프레임에 저장된 값만 사용해서 1차원 배열로 채점합니다.
print(out.values.flatten())