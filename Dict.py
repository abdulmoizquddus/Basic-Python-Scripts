#Dict are key/value pairs
drink = {"white":7 , "black": 8 , "red":9}  #key:value

print(drink)

employee= {"Finance":["bob","adam"],"IT":["gen","loise"]}  #mulitple values

print(employee)

employee["newdept"] = ["Mr. fond"]  #adding new key/value

print(employee )

employee.update({"sales":["Andire"]})  #another way

print(employee)

drink["white"] = 10

print(drink)

print(drink.get("black"))