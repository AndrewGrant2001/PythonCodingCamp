# Andrew Grant
# 105226219

dictionary = []
temp = []
count = 0
cout = 0

# Reading each line
with open('people.txt', 'r') as file1:
    for line in file1:
        for word in line.split("\n"):
            dictionary.append(word)

# This appends each string to form a 2d list
for i in range(0, len(dictionary)):
    temp.append(dictionary[i].split(","))

# This clears the files, so they do not duplicate
while True:
    for f in range(1, 4):
        stri = temp[cout][f]
        f = open(stri + ".txt", "w")
        f.close()
    cout += 2
    if cout > len(temp) - 1:
        break

# This writes the names to the files (+= 2 is due to [''] being added in every other slot, and the += 2 blocks it from
# affecting results)
while True:
    for k in range(1, 4):
        string = temp[count][k]
        f = open(string + ".txt", "a")
        f.write(temp[count][0] + "\n")
        f.close()
    count += 2
    if count > len(temp) - 1:
        break

print(f'Files are complete. :)')
