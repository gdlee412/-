import pandas as pd
file_path = 'data/data.csv' # 파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)

#열 바꾸기
df = df[['이름','국어','수학','영어']]

#행 슬라이싱
df = df[7: (len(df) - 8)]

#교수님 방식
#df = df.iloc[7:-8]
#df = df.iloc[:, 1:]


########################

print(df)



