#len
a = "i love python"
print(len(a))

#strip(): remove spaces from left side
a = "     i love python    "
print(a.strip())

#rstrip(): remove spaces from right side
print(a.rstrip())

#lstrip(): remove spaces from both sides
print(a.lstrip())


#strip(): remove character from left side
a = "###i love python###"
print(a.strip("#"))

#rstrip(): remove spaces from right side
print(a.rstrip("#"))

#lstrip(): remove spaces from both sides
print(a.lstrip("#"))

#title
b = "i love to be 2d graphics"
print(b.title())
print(b.capitalize())

#zfill

c,d,e,f = "1", "11", "111","1111"
print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#upper

g = "ossama"
print(g.upper())
print(g.lower())
