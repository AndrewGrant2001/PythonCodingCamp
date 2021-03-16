# Andrew Grant
# 105226219

num = int(input("Enter the number of terms: "))
sum = 0

for i in range(1, num + 1):
    sum = sum + (1 / i)
print(f'The sum of series is {sum}')