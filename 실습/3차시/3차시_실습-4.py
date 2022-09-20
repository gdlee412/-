score = [70, 81, 65, 67, 65, 95, 97, 78, 82, 63, 73, 56, 73, 82]
#위에 리스트는 구름 사이트에서 이미 주어질거에요 우선 간단히 적어봤어요

min = int(input())
max = int(input())

ave = 0

for i in  range(min, max + 1):
    ave += scores[i]
ave = ave / (max - min + 1)
print(ave)