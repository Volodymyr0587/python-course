dog = {"name": "Roger", "age": 3}
print(type(dog))
print(dog["name"])
dog["name"] = "Syd"
print(dog["name"])

print(dog.get("name"))
print(dog.get("color"))
print(dog.get("color", "brown"))
dog["color"] = "gray"
print(dog)

# dog.pop("name")
# print(dog)
# print(dog.popitem())

print("color" in dog)
print(dog.keys())
print(dog.values())
print(list(dog.items()))

dog["favorite food"] = "pickles"
print(dog)
print(len(dog))

del dog["color"]
print(dog)
print(len(dog))

dogCopy = dog.copy()