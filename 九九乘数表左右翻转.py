print('while循环：')
j = 1
while j <= 9:
    print('\t'*(9-j), end='')
    i = j
    while i > 0:
        print(f'{i}*{j}={i*j}\t', end='')
        i -= 1
    print()
    j += 1
print('----------------------------------------------------------------------')
print('for循环：')
for j in range(1, 10):
    for blank in range(9-j, 0, -1):  # 也可以写成print('\t'*(9-j), end='')
        print('\t', end='')
    for i in range(j, 0, -1):
        print(f'{i}*{j}={i*j}\t', end='')
    print()
