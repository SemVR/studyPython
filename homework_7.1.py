#Greeting
def say_hi(name:str, age:int):
    return f"Hi. My name is {name} and I'm {age} years old"

say_hi(str(input('Enter your first name:')), int(input('Enter your age:')))
