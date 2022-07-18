#Lists

movies = ["ok1","ok2","ok3","ok4","ok5"]

print(movies[1])   #second item
print(movies[2])   #first item
print(movies[1:4])   #item 2 to 5
print(movies[2:])   
print(movies[:])   
print(movies[-1])   
print(movies[:3])   
print(len(movies))

movies.append("ok6")
print(movies[-1])   
movies.pop()
print(movies[-1])   
movies.pop(2)
print(movies)