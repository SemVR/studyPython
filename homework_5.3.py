# Hashtag (5.3)

import string

# user_string = ['Python Community', 'i like python community!', 'Should, I. subscribe? Yes!']
user_string = [input(str('Enter to convert to hashtag: '))]

max_len = 140
for current_string in user_string:
    current_string = current_string.title()
    current_string = current_string.replace(" ", "")
    for symbol in string.punctuation:
        current_string = current_string.replace(symbol, "")

    current_string ="#" + current_string

    if len(current_string) > max_len:
        print(f" '{current_string}' has more than the maximum value, maximum length is {max_len} ")
        continue
    print(current_string)




