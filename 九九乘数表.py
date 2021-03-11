print('单while循环法：')
j = 1
i = 1
while j <= 9:
    if i < j:
        print(f'{i}*{j}={i*j}\t', end="")
        i += 1
    elif i == j:
        print(f'{i}*{j}={i*j}\t')
        j += 1
        i = 1
print('---------------------------------------------------------------------------------------')
print('双while循环法：')
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}\t', end='')
        j += 1
    print()
    i += 1
print('---------------------------------------------------------------------------------------')
print('for循环法1：')
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(f'{j}*{i}={i*j}\t', end="")
    print()
print('for循环法2：')
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i*j}\t', end="")
    print()
