input1 = int(input('Enter 1st value: '))
op = input('Enter the operator: ')
input2 = int(input('Enter 2nd value: '))
result = 0

if op == '--':
    result = input1 - (-input2)

elif op == '-':
    result = input1 - input2

elif op == '*':
    result = input1 * input2

elif op == '/':
    result = input1 / input2

print(result)
