set1 = {"Roger", "Syd", "Syd"}
print(type(set1))
print(set1) # {'Syd', 'Roger'}

set2 = {"Roger"}

# intersect = set1.intersection(set2)
intersect = set1 & set2
print(intersect)

union = set1 | set2
print(union)

diff = set1 - set2
print(diff)

subSet = set1 > set2
print(subSet)

subSet = set1 < set2
print(subSet)