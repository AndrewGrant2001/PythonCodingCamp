# Andrew Grant
# 105226219

def lowest_common_multiple(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lowest = greater
           break
       greater += 1
   return lowest


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f'The least common multiple is {lowest_common_multiple(num1, num2)}')