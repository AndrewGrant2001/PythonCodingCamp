# Andrew Grant
# 105226219

string = input("Enter word here: ")


print(string, end='')
print(string[0])

for i in range(0, len(string) - 1):
    print(string[-i + len(string) - 1] ," " * (len(string)-3), string[i+1])

for i in range(0, len(string)):
    print(string[-i], end = '')

print(string[0])