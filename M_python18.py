#tuples
myTuple = ("hicham", "berr")
print(myTuple)
print(type(myTuple))

#index
myTupleTwo = (1,2,3,4,5)
print(myTupleTwo)
print(type(myTupleTwo))
print(myTupleTwo[-1])

#tuple assign
myTupleThree = (1,2,3,4,5)
print(myTupleThree)
#myTupleThree[2]= "Three" # tuple does not accept assignment

#tuple with one element
myTuple1 = ("hicham")
myTuple2 = ("Berr")
print(myTuple1)
print(myTuple2)

print(len(myTuple1))
print(len(myTuple2))

#tuple concatenation
a = (1,2,3,4,5,6)
b = (5,6,7,8,9)

c = a + b
print(c)
d = a + ("A","B")+b
print(d)
