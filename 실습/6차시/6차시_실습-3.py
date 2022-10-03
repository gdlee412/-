import pandas as pd
file_path = 'data/data_after_2.csv' #파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)

#불리언으로 90초과만 인덱싱 한다
smart_index = df['수학'] > 90
df = df[smart_index]
smart_index = df['영어'] > 90
df = df[smart_index]
smart_index = df['국어'] > 90
df = df[smart_index]

########################

print(df)



