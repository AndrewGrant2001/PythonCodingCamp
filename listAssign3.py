# Andrew Grant
# 105226219

import random


def birthday_gen(temp, var=None):
    while True:
        var += [random.randint(1, 365)]
        for i in range(0, len(var)):
            for j in range(0, len(var)):
                if i != j:
                    if var[i] == var[j]:
                        return temp
        temp += 1


var = []
value = birthday_gen(0, var)
print(f'The first duplication was found at {value}')
