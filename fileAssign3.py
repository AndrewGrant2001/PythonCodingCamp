# Andrew Grant
# 105226219

dictionary = []
temp = []
ranks = []
count = 0
max = 0

with open('ranks.txt', 'r') as file:
    for line in file:
        for word in line.split("\n"):
            if word != '':
                ranks.append(word)

# Reading each line
with open('matches.txt', 'r') as file1:
    for line in file1:
        for word in line.split("\n"):
            if word != '':
                dictionary.append(word)

# This appends each string to form a 2d list
for i in range(0, len(dictionary)):
    temp.append(dictionary[i].split(","))

for i in range(0, len(temp)):
    for j in range(0, len(ranks)):
        if temp[i][0] == ranks[j]:
            temp[i].insert(1, str(j + 1))

for i in range(0, len(temp)):
    for j in range(0, len(ranks)):
        if temp[i][4] == ranks[j]:
            temp[i].insert(5, str(j + 1))

for g in range(0, len(ranks)):
    num = len(ranks[g])
    if num > max:
        max = num


print(f'Underdog{(max - 8) * " "}Rank  Score  Bets   vs    Favourite            Rank  Score  Bets')


for x in range(0, len(temp)):
    if int(temp[x][1]) < int(temp[x][5]) and int(temp[x][2]) < int(temp[x][6]) and (int(temp[x][5]) - int(temp[x][1])) > 10 \
            and (float(temp[x][7]) / (float(temp[x][3]) + float(temp[x][7]))) > 0.8:
        print(f'{temp[x][4]}{" " * (max - len(temp[x][4]))}'
              f'{" " * (3 - len(temp[x][5]))}{temp[x][5]}'

              f'   {" " * (4 - len(temp[x][6]))}{temp[x][6]}'

              f'   {" " * (4 - len(temp[x][7]))}{temp[x][7]}'

              f'   vs.  {temp[x][0]}{" " * (max - len(temp[x][0]))}'

              f'{" " * (3 - len(temp[x][1]))}{temp[x][1]}'

              f'   {" " * (4 - len(temp[x][2]))}{temp[x][2]}'

              f'   {" " * (4 - len(temp[x][3]))}{temp[x][3]}')
    elif int(temp[x][1]) > int(temp[x][5]) and int(temp[x][2]) > int(temp[x][6]) and (int(temp[x][1]) - int(temp[x][5])) > 10 \
            and (float(temp[x][3]) / (float(temp[x][3]) + float(temp[x][7]))) > 0.8:
        print(f'{temp[x][0]}{" " * (max - len(temp[x][0]))}'

              f'{" " * (3 - len(temp[x][1]))}{temp[x][1]}'

              f'   {" " * (4 - len(temp[x][2]))}{temp[x][2]}'

              f'   {" " * (4 - len(temp[x][3]))}{temp[x][3]}'

              f'   vs.  {temp[x][4]}{" " * (max - len(temp[x][4]))}'

              f'{" " * (3 - len(temp[x][5]))}{temp[x][5]}'

              f'   {" " * (4 - len(temp[x][6]))}{temp[x][6]}'

              f'   {" " * (4 - len(temp[x][7]))}{temp[x][7]}')

