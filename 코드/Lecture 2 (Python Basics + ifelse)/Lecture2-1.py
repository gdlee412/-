USD = 1200
CAD = 900
EUR = 1300

print("[오늘의 환율]\n1. USD: 1,200원\n2. CAD: 900원\n3. EUR: 1300원\n")

KRW = int(input("고객 원화 보유량 : "))
choice = int(input("환전 통화 선택 (1-3): "))

if choice == 1:
    print("환전 통화: USD")
    rate = USD
elif choice == 2:
    print("환전 통화: CAD")
    rate = CAD
else:
    print("환전 통화: EUR")
    rate = EUR
change = KRW // rate
use_KRW = change * rate
remain_KRW = KRW - use_KRW
print("최대환전 가능 금액(EUR):", change)
print("환전에 소요된 원화량 (KRW):", use_KRW)
print("고객원화 잔액 (KRW):", remain_KRW)