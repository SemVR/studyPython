# Move item in list (3.2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = numbers.copy()
if len(new_numbers) > 0:
    new_numbers.insert(0, numbers[-1])
    new_numbers.pop()
print(numbers)
print(new_numbers)