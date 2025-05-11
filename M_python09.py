#lesson strings
#index(substring, start, end)
a="I love python"
print(a.index("p"))

#rjust
c = "hicham"
print(c.rjust(12,"#"))

#splitlines

e = """ first line 
second line 
third line"""
print(e.splitlines())

f = "First line \nSecond line\nThird line"
print(f.splitlines())

#expendtabs()
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(1))

one = "I Love Python And 3G"
two = "I love python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""

print(three.isspace())
print(four.isspace())

five = "i love python"
six = "I Love Python"
print(five.isupper())
print(five.islower())
print(six.isupper())
print(six.islower())
print(six.istitle())


