count = 0
lis = []

num = int(input('Enter the length of list: '))

for i in range(num):
    lis.append(int(input('Enter the number: ')))

for j in range(num):
    if lis[j] % 2 == 0:
        count += 1

print(count)
