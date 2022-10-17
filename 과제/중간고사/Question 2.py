party = {
	"강민" : "콜라",
	"홍진호" : "카라멜마끼아또",
	"김동수"	:	"아메리카노",
	"김택용" :	"카라멜마끼아또",
	"박성준"	:	"사이다",
	"박용욱"	:	"사이다",
	"박정석"	:	"우유",
	"박태민"	:	"아인슈페너",
	"서지훈"	:	"우유",
	"송병구"	:	"우유",
	"오영종"	:	"아인슈페너",
	"이영호"	:	"콜라",
	"진달래"	:	"카라멜마끼아또",
	"이윤열"	:	"콜라",
	"이제동"	:	"콜라",
	"임요환"	:	"카라멜마끼아또",
	"정명훈"	: "아인슈페너",
	"조용호"	:	"사이다",
	"최연성"	: "아인슈페너",
	"허영무"	:	"사이다"
}

#empty dictionary and count for names not included
drink_list = {}
not_part = 0

#while loop
while True:
	#input
	name = input()
	#if '종료',  break from loop
	if name == '종료':
		break
	#if name in party
	if name in party:
		drink_name = party[name]
		#if drink was already taken count previously, increment
		if drink_name in drink_list:
			drink_list[drink_name] += 1
		#if drink was never made in dict, create dict with value 1
		else:
			drink_list[drink_name] = 1
	#if name not part of party dict, increase not_part count
	else:
		not_part += 1

#print out the keys and values of drink_list in order with format
for keys in drink_list:
	print("{} {} 잔".format(keys, drink_list[keys]))
	
#if not_part exists, print with format
if not_part > 0:
	print("취향을 모르는 사람 {} 명".format(not_part))
