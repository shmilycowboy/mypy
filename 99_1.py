j = 1
i = 1
while j <= 9: 
    if i == j:
        print(f'{i}*{j}={i*j}\t')
        j += 1
        i = 1
    elif i < j:
        print(f'{i}*{j}={i*j}\t', end="")
        i += 1
