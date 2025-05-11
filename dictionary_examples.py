# create a dictionary
person = {
    "name" : "Hicham",
    "age" : 38,
    "city" : "Denver"
}

#Accessing values by key
print(person["name"])       #output : Hicham
print(person.get("age"))    #output : 38

#modifying values
person["age"] = 30  # modify value
person["email"] = "Hicham@example.com" # ad new key-value

# Removing items
person.pop("city")
del person["name"]

#Loop through dictionary
for key, value in person.items():
    print(key, "=>", value)

#check if a key exists
if "email" in person:
    print("Email found")

#method to know
person.keys()     #Return all keys
person.values()   #Return all values
person.items()    #Return all key-value pairs

book = {
    "title" : "Python Basics",
    "author" : "John Doe",
    "year" : 2023
}

print(book["title"])

#add key-value
book["pages"] = 250

#Loop through dictionary
for key, value in book.items():
    print(key, "=>", value)

