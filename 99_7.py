i = j = 1
print('\t'*(9-j), end='')
while j <= 9:
    if i == 1:
        print(f'{i}*{j}={i*j}\t')
        j += 1
        i = j
        print('\t'*(9-j), end='')
    while i > 1 and i < 10:
        print(f'{i}*{j}={i*j}\t', end='')
        i -= 1
