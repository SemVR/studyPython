# Split one list into two lists (3.3)
numbers = []

middle_index = len(numbers)//2
if len(numbers) % 2 != 0:
    middle_index += 1
first_list = numbers[:middle_index]
second_list = numbers[middle_index:]
print(first_list)
print(second_list)
result = [first_list, second_list]
print(result)