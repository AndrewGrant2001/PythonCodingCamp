# Andrew Grant
# 105226219

def subtract(list1, list2):
    new_list = []
    for i in range(0, len(list1)):
        count = 0
        for j in range(0, len(list2)):
            if list1[i] != list2[j]:
                count += 1
        if count == len(list2):
            new_list += [list1[i]]
    return new_list

big_list = []
small_list = []

while True:
    temp = int(input("Enter numbers of first list (-1 to stop): "))
    if temp == -1:
        break
    else:
        big_list += [temp]

print("-----------------------------------------------------------")

while True:
    temp = int(input("Enter numbers of second list (-1 to stop): "))
    if temp == -1:
        break
    else:
        small_list += [temp]

final_list = subtract(big_list, small_list)

print(f'The new list generated from the first minus the second is {final_list}')