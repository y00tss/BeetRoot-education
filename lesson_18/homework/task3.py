def iterat(start, end, step=1):
    for i in range(start, end, step):
        yield i


a = []
for i in iterat(1, 10):
    a.append(i)

print(a)


# наверное не понял задание. Нужно было придумать новый способ перебора?