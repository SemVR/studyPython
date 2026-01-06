# The simplest calculator
number_1 =int(input("Enter the first number: "))
number_2 =int(input("Enter the second number: "))
math_operation = input("Choose a mathematical operation(+, -, *, /): ")
if math_operation == "+":
    print (f"Result: {number_1 + number_2}")
if math_operation == "-":
    print (f"Result: {number_1 - number_2}")
if math_operation == "*":
    print (f"Result: {number_1 * number_2}")
if math_operation == "/":
    if number_1 and number_2 > 0:
        print (f"Result: {number_1 / number_2}")
    else:
        print ("The number must not be equal to zero")
else:
    print ("Done")