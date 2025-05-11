#Dictionary
#clear
from setuptools.package_index import user_agent

from type_check import skills

user = {
    "name": "hicham"
}
print(user)
print(user.clear())
print(user)
print("=" * 50)

#update
member = {
    "name": "hicham",
}
print(member)
member["age"] = 38
print(member)
member.update({"country":"Morocco"})
print(member)
print("=" * 50)

main = {
    "name": "hicham",
}
b = main.copy()
print(main)
print(b)
main.update({"lastName":"Berr"})
print(main)
print(b)
print("=" * 50)
#setDefault
user2 = {
    "name": "hicham",
}
print(user2)
print(user2.setdefault("age", 38))
print(user2)
print("=" * 50)

#popitem
member2 ={
    "name": "hicham",
    "age": 38,
}
print(member2)
member2.update({"skills" : "good"})
print(member2.popitem())
print("=" * 50)

#fromkeys
a = ('myKeyOne', 'myKeyTwo', 'myKeyThree')
b = "x"
print(dict.fromkeys(a,b))
print("=" * 50)


