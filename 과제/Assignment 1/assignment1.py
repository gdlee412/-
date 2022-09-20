def fruit_discount(market, discount):
	#strawberry discount
	if strawberry[0] >= 20:
		discount["strawberry"] = 220
	elif strawberry[0] >= 10:
		discount["strawberry"] = 270
	#carrot discount
	if carrot[0] >= 20:
		discount["carrot"] = 370
	elif carrot[0] >= 10:
		discount["carrot"] = 450
	#watermelon discount
	if watermelon[0] >= 3:
		discount["watermelon"] = 1600
	#melon discount
	if melon[0] >= 5:
		discount["melon"] = 800

market = {"strawberry":[0, 300], "carrot":[0, 500], "watermelon":[0, 2000],"melon":[0, 1000]}
#for discount price
discount = {"strawberry":300, "carrot":500, "watermelon":2000,"melon":1000}
#convenience purposes
total_price = 0
discount_price = 0
strawberry = market["strawberry"]
watermelon = market["watermelon"]
carrot = market["carrot"]
melon = market["melon"]

#while loop
while True:
	initial_input = int(input("0 : calculate, 1 : add\n"))
	#if input is 0, print variables and break from loop
	if initial_input == 0:
		print("Here is recipt. Total price is {}. Discount price is {}.".format(total_price, discount_price))
		break
	#otherwise, ask for fruit input
	else:
		fruit = input()
		#variable to check if fruit is part of key
		not_fruit_count = 0
		#for loop to check whether fruit exists in the market
		for key in market:
			#if fruit is a key, ask for number of fruits
			if fruit == key:
				fruit_number = int(input())
				#add the number of fruits
				market[fruit][0] += fruit_number
			#else, just increase not fruit count
			else:
				not_fruit_count += 1

		#if not fruit count = 4, fruit does not exist in dictionary, so print no product
		if not_fruit_count == 4:
			print("no product in market")

		print("strawberry : {}, carrot : {}, watermelon : {}, melon : {}".format(strawberry[0], carrot[0], watermelon[0], melon[0]))

		#update discount price
		fruit_discount(market, discount)
		total_price = 0
		discount_price = 0
		for key in market:
			#calculate total price
			total_price += market[key][0] * market[key][1]
			#calculate discount price
			discount_price += market[key][0] * discount[key]
	