# Andrew Grant
# 105226219

dictionary = []
left_overs = []
story = []
count = 0

# This is very slow, no infinite loops. Just give it a minute and it does the job! :)

with open('dictionary.txt', 'r') as file1:
    for line in file1:
        for word in line.split():
            dictionary.append(word)

with open('story.txt', 'r') as file2:
    for line in file2:
        for word in line.split():
            story.append(word)

for i in range(0, len(story)):
    if story[i] not in dictionary:
        left_overs.append(story[i])

print(left_overs)