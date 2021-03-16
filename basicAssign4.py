#Andrew Grant
#105226219

num_to_add = int(input("Enter a number: "))
result = 0
temp = num_to_add

while num_to_add > 0:
    rem = num_to_add % 10
    result = result + rem
    num_to_add = int(num_to_add/10)

print(f'Sum of all the digits of the number {temp} is equal to {result}')