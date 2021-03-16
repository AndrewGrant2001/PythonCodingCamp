# Andrew Grant
# 105226219

import random

names = []
temp = ""

while True:
    temp = input("Enter name (x to generate): ")
    if temp == 'x':
        break
    else:
        names.append(temp)

random.shuffle(names)

print("Generating Secret Santa gift exchange....")
print(names[len(names) - 1], "gifts", names[0])

for i in range(0, len(names) - 1):
    print(names[i], "gifts", names[i + 1])
