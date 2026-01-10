# Move all zeros to the end of the list (4.1)
numbers = [0, 1, 0, 12, 3]

i = 0

for numb in numbers:
    if numb != 0:
        numbers[i] = numb
        i += 1
for numb in range(i, len(numbers)):
    numbers[numb] = 0

print(numbers)


