# Andrew Grant
# 105226219

num = 0
i = 0
total = 0
nums = []

while num != -1:
    num = int(input("Enter numbers (-1 to stop): "))
    nums += [num]

nums.sort(reverse=True)

for i in range(0, 6):
    total += nums[i]
    i += 1

print(f'The average is {total / 6}')
print(f'The median is: {(nums[2] + nums[3]) / 2}')