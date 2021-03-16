# Andrew Grant
# 105226219

month_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

months = int(input("Enter month: "))
day = int(input("Enter day: "))
i = 0
total = day

while i < (months - 1):
    total += month_days[i]
    i += 1

print(f'That is day {total} of the year.')