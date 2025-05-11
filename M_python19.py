# set
mySetOne = {"hicham", "Berr", 100,233}
print(mySetOne)
#print(mySetOne[0:2]) #set is not subscriptable and is not indexable
#items must be unique
mySetTwo = {"hicham", "Berr", 100,100,"hicham"}
print(mySetTwo)

#union
e = {"malek", "berr", 7, 14}
k = {1,2,3}
print(e | k)
print(e.union(k))

#add
s = {1,2,3}
s.add(4)
print(s)

#difference
l = {1,2,3,4}
m = {1,2,5,6}
print(l.difference(m))
