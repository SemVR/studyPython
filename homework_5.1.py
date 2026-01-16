# Variable name (5.1)
import string
import keyword

# variable_names = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value','Get_value', 'get_Value', '3m', 'm3', 'assert', 'assert_exception']

while True:
    variable_names = [input(str("Enter your variable name: "))]

    for variable_name in variable_names:
        if len(variable_name) == 0:
            print("Incorrect variable length!")
            continue

        if variable_name in keyword.kwlist:
            print(f"Error! Found '{variable_name}' is keywords list!")
        elif variable_name.find("__") != -1:
            print(f"Error! Found double '_' in '{variable_name}' variable name!")
        elif (not variable_name[0].isnumeric()
              and variable_name.find(" ") == -1):
            is_correct = True
            restricted_symbols = string.punctuation.replace("_", "")
            restricted_letters = string.ascii_uppercase

            for symbol in variable_name:
                if symbol in restricted_letters or symbol in restricted_symbols:
                    is_correct = False
                    print(f"Error! Found '{variable_name}' in variable name!")
                    break
            else:
                print(f"Keyword '{variable_name}' is correct!!!")
        else:
            print(f"Error! Found '{variable_name}' in variable name!")

    finish_check = input('Enter "-" to finish or "Enter" button to continue:')
    if finish_check == "-":
        break