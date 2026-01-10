#List of 3 items (4.3)
import random


# numbers = []
# for i in range(random.randint(1, 10)):
#     numbers.append(random.randint(0, 10))
# print(numbers)
# result = [
#     numbers[0],
#     numbers[2],
#     numbers[-2],
# ]
# print (result)



len_list = random.randint(3,10)
numbers = [random.randint(3,10) for _ in range(len_list)]
print(numbers)
result = [
    numbers[0],
    numbers[2],
    numbers[-2],
]

print(result)