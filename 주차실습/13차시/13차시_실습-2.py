# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
test_set = [list(map(int, input().split())) for _ in range(5)]
test_label = list(map(int, input().split()))
#input에 의한 test set 정의입니다. 신경안쓰셔도 됩니다.

########################################코드##########################################
from sklearn.linear_model import LinearRegression

x = [[1],[0],[-2],[3],[-4],[5],[-6],[7],[-8]]
y = [3,2,6,11,18,27,38,51,66]

lr = LinearRegression()

lr.fit(x, y)

y_pred = lr.predict(test_set)
print(y_pred)

#####################################################################################
print( lr.coef_, lr.intercept_ )
print(lr.score(test_set, test_label))