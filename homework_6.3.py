#Product of numbers
while True:

    number = int(input("Enter a number: "))

    while number > 9:
            temp_number = str(number)
            number = 1
            for char in temp_number:
                if char.isdigit():
                    number *= int(char)
            print(number)

    finish = input("Enter '-' to exit or 'Enter' button to continue:")
    if finish == "-":
        break