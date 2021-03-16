# Andrew Grant
# 105226219

input_string = input("Enter you string to be reversed: ")

string_reversed = ''

for c in input_string:
    string_reversed = c + string_reversed

print('Reverse String using for loop =', string_reversed)