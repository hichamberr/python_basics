#Declare strings
first_name = "Hicham"
last_name = "Berr"

#concatenate strings
full_name = first_name + " " + last_name
print("Full Name is : ", full_name)

#insert value into a string f-strings (formatted strings)
print(f"Hello, {full_name}! Welcome to Python.")

#string methods
print(full_name.upper())
print(full_name.lower())
print(full_name.startswith("Hi"))
print(full_name.endswith("rr"))
print("Name lenght:", len(full_name))

#Indexing and slicing
print(full_name[0]) # print the first character
print(full_name[-1]) #print the last character
print(full_name[1:-2])  # substring (character 0 to 5)


