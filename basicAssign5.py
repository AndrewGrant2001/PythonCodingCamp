# Andrew Grant
# 105226219

print("Enter the points below:")
x_1 = int(input("x1: "))
y_1 = int(input("y1: "))
x_2 = int(input("x2: "))
y_2 = int(input("y2: "))

slope = (y_2 - y_1)/(x_2 - x_1)

b = y_2 - (slope)*(x_2)

print("Enter below the point to check if it is on the line: ")

x_input = int(input("x-coordinate: "))
y_input = int(input("y-coordinate: "))
print("Checking your point....")

if y_input == ((slope)*(x_input) + b):
    print(f'The point ({x_input},{y_input}) is on the line y = {slope}x + {b}!!!')
else:
    print(f'The point ({x_input},{y_input}) is not on the line y = {slope}x + {b} :(')