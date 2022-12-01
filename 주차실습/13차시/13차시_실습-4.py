# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

########################################코드##########################################

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import pandas as pd

lr = LinearRegression()
lr2 = LinearRegression()
lr3 = LinearRegression()

boston = load_boston()
dataset = pd.DataFrame(boston.data, columns = boston.feature_names)
dataset['mid_price'] = boston.target

train_set = dataset.iloc[100:]
test_set = dataset.iloc[:100]

train_X = train_set.drop(['mid_price'], axis=1)
train_Y = train_set['mid_price']

test_X = test_set.drop(['mid_price'], axis=1)
test_Y = test_set['mid_price']

lr.fit(train_X, train_Y)

coef = pd.Series(data=lr.coef_, index = train_X.columns) * 1000
coef = coef.sort_values(ascending=False)
print(coef)
coef = coef.sort_values(ascending=False, key=abs)

tail_col = coef.index.values[-5:]

dataset2 = dataset.drop(tail_col,axis=1)
train_set2 = dataset2.iloc[100:]
test_set2 = dataset2.iloc[:100]

train_X2 = train_set2.drop(['mid_price'], axis=1)
train_Y2 = train_set2['mid_price']

test_X2 = test_set2.drop(['mid_price'], axis=1)
test_Y2 = test_set2['mid_price']

lr2.fit(train_X2, train_Y2)

tail_col = coef.index.values[-2:]

dataset3 = dataset[['CRIM', 'INDUS', 'CHAS', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'mid_price']]

train_set3 = dataset3.iloc[100:]
test_set3 = dataset3.iloc[:100]

train_X3 = train_set3.drop(['mid_price'], axis=1)
train_Y3 = train_set3['mid_price']

test_X3 = test_set3.drop(['mid_price'], axis=1)
test_Y3 = test_set3['mid_price']

lr3.fit(train_X3, train_Y3)

print(lr.score(train_X, train_Y))
print(lr.score(test_X, test_Y))

print(lr2.score(train_X2, train_Y2))
print(lr2.score(test_X2, test_Y2))

#####################################################################################
#마지막 모델은 lr3라는 이름으로 정의하고 학습을 해주세요.
print(lr3.score(train_X3, train_Y3))
print(lr3.score(test_X3, test_Y3))