# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
test_set = [list(map(int, input().split())) for _ in range(1)]
test_set2 = [[test_set[0][0]]]
#test set을 위한 input입니다. 신경쓰지마세요


########################################코드##########################################
from sklearn.linear_model import LinearRegression

X = [[171,0],[169,0],[176,0],[168,0],[181,0],[166,0],[180,0],[175,0],
     [163,1],[162,1],[171,1],[162,1],[164,1],[162,1],[158,1],[173,1]]
X2 = [[171],[169],[176],[168],[181],[166],[180],[175],
     [163],[162],[171],[162],[164],[162],[158],[173]]
Y = [69,65,72,67,71,65,80,71,55,51,59,53,61,56,47,57]

lr = LinearRegression()
lr2 = LinearRegression()

lr.fit(X,Y)
lr2.fit(X2,Y)

y_pred = lr.predict(test_set)
y_pred2 = lr2.predict(test_set2)
#####################################################################################
print(lr.score(X, Y), lr2.score(X2, Y))
print(y_pred, y_pred2)