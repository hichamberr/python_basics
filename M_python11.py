#------String Formatting-----
name = "Hicham"
age = 38
rank = 10

print("my name is " + name + "and my age is " + str(age) + "and my rank is " + str(rank))

print("my name is : %s" % name)
print("my age is %d" % age)
print("my rank is %d" % rank)

print("my name is %s and my age is %d and my rank is %f" % (name, age, rank))

# %s : string
# %d : Number
# %f : float

n = "hicham"
l = "python"
y = 10

print("My name is %s I am %s Developer with %d years of Experience" % (n, l, y))

myNumber = 10
print("My Number is : %d" % myNumber)

# Truncate string
myLongString = "Hello World I am studying python to be the greater developer in the world"
print("Message is : %s" % myLongString)
print("Message is : {:.5s}".format(myLongString))

# NEW WAY OF STRING

print("my name is : {:s} and my age is {:d} and my rank is {:f}".format(name, age, rank))

#control floating point number
myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is : {:f}".format(myNumber))
print("My Number is : {:.2f}".format(myNumber))

myMoney = 10000000
print("My Money in bank is {}".format(myMoney))
print("My Money in bank is: {:_d}".format(myMoney))
print("My Money in bank is: {:,d}".format(myMoney))

a, b, c = "one", "two", "three"
print("Hello {} {} {}".format(a, b, c))
print("Hello {1} {2} {0}".format(a, b, c))
print("Hello {2} {0} {1}".format(a, b, c))

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {1:f} {0:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))


