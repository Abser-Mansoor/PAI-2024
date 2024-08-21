lis = []
num = int(input('Enter the length of list: '))
lim = int(input('Enter the limit: '))

for i in range(num):
    lis.append(int(input('Enter the number: ')))

lis = [x for x in lis if x >= lim]

print("Modified list: ", lis)
