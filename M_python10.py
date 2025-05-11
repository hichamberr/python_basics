# replace old value by the new value and count

a = "Hello one two three one one "

print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))
print(a.replace("one", "1", 3))

myList = ["Hicham", "Berr", "Malek"]
print("-".join(myList))
print(",".join(myList))
print("/".join(myList))
print(type(", ".join(myList)))
