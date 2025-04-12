from functools import reduce

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#//% MAP
power_of_two = list(map(lambda num: num ** 2, numbers))
print(power_of_two)

#//% FILTER
even = list(filter(lambda num: num % 2 == 0, numbers))
print(even)

odd = list(filter(lambda num: num % 2 != 0, numbers))
print(odd)

#//% REDUCE
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

total_sum = reduce(lambda a, b: a[1] + b[1], expenses)   
print(total_sum)


def sum_by_key(data, key):
    return sum(item[key] for item in data)

expenses = [
    {'name': 'Dinner', 'amount': 80},
    {'name': 'Car repair', 'amount': 120},
    {'name': 'Insurance', 'amount': 200}
]

total = sum_by_key(expenses, 'amount')
print(total)  # Output: 400

