# 1 (number to square)
# number  = int(input("Enter a number, I will square it: "))
# numb_to_square = number ** 2
# print(f"Result:{numb_to_square}")


#2 (average of three numbers)
# number_1 = int(input("Enter a number first: "))
# number_2 = int(input("Enter a number second: "))
# number_3 = int(input("Enter a number third: "))
#
# result = (number_1 + number_2 + number_3)/3
# print(f"The average of these numbers: {result}")


#3 (convert minutes to hours)
# number = int(input("Enter minutes and I will convert it to hours and minutes: "))
# hour = number//60
# minute = number%60
# print(f"Time after conversion:{hour}-Hours,{minute}-Minutes!")


#4 (discount calculation)
# price = int(input("Enter a price: "))
# discount_user = int(input("Enter the discount %: "))
# result = price - (price * discount_user /100)
# print(f"Your price with discount: {result}")

#5 (last digit of the number)
# number  = int(input("Enter a number: "))
# result = number%10
# print(result)

#6 (perimeter of a rectangle)
# length = int(input("Enter the length of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))
# perimeter = (length + width) * 2
# print(f"Perimeter according to given data = {perimeter}")


#7 (outputting a number to a column)
# number = int(input("Enter a 4-character number: "))
# numb_1 = number // 1000
# numb_2 = number //100 %10
# numb_3 = number //10 %10
# numb_4 = number % 10
# print(numb_1)
# print(numb_2)
# print(numb_3)
# print(numb_4)
#
# number_v2 = int(input("Enter a 4-character number: "))
# numb_1v2, rest = divmod(number_v2, 1000)
# numb_2v2, rest = divmod(rest, 100)
# numb_3v2, numb_4v2 = divmod(rest, 10)
# print(numb_1v2)
# print(numb_2v2)
# print(numb_3v2)
# print(numb_4v2)