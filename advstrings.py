#!/bin/python3
myname = "Abdul"
print(myname[0])
print(myname[-1])

Sentence = "This is a sentence"

print(Sentence[:4])   #4 is exclusive
print(Sentence.split())    #by default delimiter is space

sen_split = Sentence.split()
sen_join = ' '.join(sen_split)
print(sen_join)

quote1 = "He said, 'give me money'"  
quote2 = "He said, \"give me money\""  #for mult quotations  

print(quote1)
print(quote2)

too_much_space = "            helllo"
print(too_much_space.strip())

print("a" in "apple")   #case sensitive

letter ="A"
word = "Apple"
print(letter.lower() in word.lower())

movie = "Alpha"

print("I like "+movie)
print("I like {}".format(movie))   #same like last, using place holder
