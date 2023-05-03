list100 = []
list_result = []

# 1 way (bad)
# for i in range(1, 101):                                                                                               # code was performed through "for" to decrease code lines but its load the memory
#     list100.append(i)

list100 = list(range(1, 101))                                                                                           # minus 200 actions of Python


i = 0
while i < 100:
    if (list100[i] % 7) == 0 and (list100[i] % 5) != 0:
        list_result.append(i + 1)                                                                                       # why + 1? Cos difference between index and item. List item from 1, index from 0
    i += 1

print(*list_result)                                                                                                     # "*" to show list without []