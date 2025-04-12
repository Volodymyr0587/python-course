""" condition = True

while condition:
    print("The condition is True")
    condition = False """
    
""" count = 0
while count < 10:
    print("The condition is True")
    count += 1
    
print("After the loop") """

""" items = [1, 2, 3, 4, 5]
for item in items:
    print(item) """
    
""" for i in range(10):
    print(i) """
    
""" items = ["John", 43, "plummer"]
for idx, item in enumerate(items):
    print(idx, item) """
    
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 2:
        continue
    print(item)
print("=============")
for item in items:
    if item == 3:
        break
    print(item)