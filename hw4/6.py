from itertools import count, cycle

a = int(input('Введите любое целое число: '))

for i in count(a):
    if i > 1000:
        break
    print(i)

b = [3, 4, 5]
count = 0
for i in cycle(b):
    if count > 50:
        break
    print(i)
    count += 1
