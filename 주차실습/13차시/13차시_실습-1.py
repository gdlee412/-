# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
test_set = [list(map(int, input().split())) for _ in range(5)] #input test set 정의. 문제 푸는데 신경 안쓰셔도 됩니다.

########################################코드##########################################
#print(test_set) #test set 확인용, 이론 교안과 같은 set의 형태입니다.
#linear regression 학습을 진행해주세요.
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

x = [[1],[0],[-5],[10],[-20],[42],[-16],[-9],[8]]
y = [10,7,-8,37,-53,133,-41,-20,31]

lr.fit(x,y)

#####################################################################################
y_pred = lr.predict(test_set)
print(y_pred)
print( lr.coef_, lr.intercept_ )