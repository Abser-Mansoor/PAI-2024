sum = 0
lis = []

num = int(input('Enter the length of list: '))

for i in range(num):
    lis.append(int(input('Enter the number: ')))

for j in range(num):
    sum += lis[j]

print(sum)
