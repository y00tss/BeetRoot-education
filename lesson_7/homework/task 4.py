import datetime
week_num = {}
num_week = {}
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(1, len(weekdays)):
    week_num.update({weekdays[i]: i})
for i in range(1, len(weekdays)):
    num_week.update({i: weekdays[i]})

print(*weekdays, sep=", ")
print(num_week)
print(week_num)



