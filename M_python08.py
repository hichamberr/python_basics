# split() and rsplit
a = "i love python and PHP"
print(a.split())

b = "i-love-python-and-PHP"
print(b.split('-'))

#max split
c = "i-love-python-and-PHP"
print(b.split('-', 2))

#rsplit
d = "i-love-python-and-PHP"
print(d.rsplit('-',3))

# center
e = "Hicham"
print(e.center(9))
print(e.center(9,"#"))
print(e.center(15,"#"))

f = "i love python and PHP"
print(f.count("PHP"))
print(f.find("PHP", 0 , 25))

#swapcase
g = "i love python"
print(g.swapcase())

#starts with
i = "I love python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("p", 7, 112))

#endswith
j = "i love python"
print(j.endswith("n"))
print(j.endswith("s"))
print(j.endswith("p", 7,12))



