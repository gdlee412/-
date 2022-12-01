import pandas as pd

df = pd.read_csv('data/winequality-red-converted.csv',dtype=float) # quality가 0 1으로 변환된 데이터입니다

df_test = df[:300]
df = df[300:]

#############################코드 ####################################
# colab 등에서 데이터를 시각화하는 등 자유롭게 전처리를 진행하고 모델을 성능을 올려봅시다.
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000)

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df_test.drop_duplicates(inplace=True)
df_test.dropna(inplace=True)

x = df.drop(['quality'], axis = 1)
y = df['quality']

test_x = df_test.drop(['quality'], axis = 1)
test_y = df_test['quality']

lr.fit(x, y)
#################################################################
#####################################교수님 코드###############################
df.drop(['ph'], axis - 1, inplace = True)
df_test.drop(['ph'], axis - 1, inplace = True)

df.drop(df.loc[df['total sulfur dioxide'] > 160].index, axis = 0, inplace = True)
df.drop(df.loc[df['free sulfur dioxide'] > 50].index, axis = 0, inplace = True)

x = df.drop(['quality'], axis = 1)
y = df['quality']

test_x = df_test.drop(['quality'], axis = 1)
test_y = df_test['quality']

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000)

lr.fit(x, y)

##########################################################################
train_score = lr.score(x, y)
test_score = lr.score(test_x,test_y)
train_pass = False
test_pass = False

if(train_score >= 0.735):
	train_pass = True


if(test_score >= 0.715):
	test_pass = True
print(train_pass,test_pass)