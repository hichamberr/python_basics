# Create a list
fruits = ["apple", "banana", "cherry"]

#Access items
print(fruits[0])       #Output: apple
print(fruits[-1])      #Output: cherry (last item)

#modify an item
fruits[1] = "orange"
print(fruits)         # ['apple', 'orange', 'cherry']


#Add new items
fruits.append("kiwi")
fruits.insert(1, "mango")
print(fruits)

#Remove items
fruits.remove("apple")   # Remove by value
fruits.pop()             #Remove last item
print(fruits)

#Length of list
print((len(fruits)))

#loop through list
for fruit in fruits:
    print(fruit)
