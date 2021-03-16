# Andrew Grant
# 105226219

value = 1
count = 0
total = 0
max = 0

while True:
    value = int(input("Enter number here (0 to stop): "))
    if value == 0:
        break
    else:
        total += value
        if max < value:
            max = value
        if count == 0:
            min = value
        elif min > value:
            min = value
        count += 1

print(f'''
The average is {total / count}
The minimum value is {min}
The maximum value is {max}''')
