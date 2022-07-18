#!/bin/python3

def drink(money):
	if money >= 2 :
		return "Buy Drink"
	else:
		return "No Enough money"

print(drink(3))
print(drink(1))


def alochol(age,money):
	if(age>=21) and (money>=5):
		return "Get Drink"
	elif (age>=21) and (money<5):
		return "Less money"
	elif (age<21) and (money>=5):
		return "Kid"
	else:
		return "Too young and less money"

print(alochol(25,5))
print(alochol(20,5))
print(alochol(25,3))
