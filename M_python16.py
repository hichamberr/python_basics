#append()
from os import remove

myFriends = ["Hicham", "Malek", "Houda"]
print(myFriends)
myFriends.append("malak")
print(myFriends)
myFriends.append(True)
print(myFriends)

#extend()
a = [1,2,3,4,5]
b = ["a","b","c","d"]

a.extend(b)
print(a)

#remove()
x = [1,2,3,4,5]
x.remove(3)
print(x)

#sort()
y = [1,3,5,8,6,20,15,10]
y.sort()
print(y)

