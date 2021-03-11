print('单while循环法：')
i, j = 1, 9
while j >= 1:
    if i < j:
        print(f'{i}*{j}={i*j}\t', end='')
        i += 1
    elif i == j:
        print(f'{i}*{j}={i*j}\t')
        j -= 1
        i = 1
print('--------------------------------------------------------------------------')
print('双while循环法：')
j = 9
while j > 0:
    i = 1
    while i <= j:
        print(f'{i}*{j}={j*i}\t', end='')
        i += 1
    j -= 1
    print()
print('--------------------------------------------------------------------------')
print('for循环法：')
for j in range(9, 0, -1):
    for i in range(1, j+1):
        print(f'{i}*{j}={j*i}\t', end='')
    # for blank in range(9-j):
    #    print('\t', end='')
    print()
