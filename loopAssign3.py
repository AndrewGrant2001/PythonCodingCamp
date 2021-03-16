# Andrew Grant
# 105226219

string = input("Enter text here: ")
string2 = string

string = " ".join(string.split())

print(f'Done with built in function: {string}')

i = 0
while i < len(string2):
    if string2[i] == " ":
        if i + 1 != len(string2):
            if string2[i + 1] == " ":
                string2 = string2[:i] + string2[i+1:]
            else:
                i += 1
        else:
            break
    else:
        i += 1

print(f'Done with while loop: {string2}')