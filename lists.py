""" 
items = ["Roger", 1, "Syd", "Quincy", 7, True]

print("Roger" in items) # True
print("Beau" in items) # False
print(items[2]) # Syd
items[2] = "Beau"
print(items[2]) # Beau
print(items[-1]) # True

print(items[2:4]) # ["Beau", "Quincy"]
print(items[2:]) # ['Beau', 'Quincy', 7, True]
print(items[:3]) # ["Roger", 1, "Beau"]

items.append("Ball")
print(items)

items.extend([8, 9, 10])
print(items)

items += [11, 12, 13]
print(items)

items.remove("Roger")
print(items)

print(items.pop())
print(items) 
items.insert(2, "TEST")
print(items) 
"""


# SORTING LISTS
items = ["Roger", 1, "Syd", "bob", "Alma", "Quincy", 7, True]

# filter items list (only strings)
items = list(filter(lambda item: isinstance(item, str),  items))

# make list copy 
items_copy = items[:]

items.sort(key=str.lower)
print(items)
print(items_copy)

sorted(items, key=str.lower)
print(items)