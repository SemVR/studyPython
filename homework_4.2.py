# Find the sum of elements with even indices(4.2)

numbers = []

if numbers:
    sum_number = sum(numbers[::2])
    print(sum_number)
    result = sum_number * numbers[-1]
    print(result)
else:print(0)




