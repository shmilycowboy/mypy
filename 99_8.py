for col in range(1, 10):
    print('\t'*(9-col), end='')
    for line in range(col, 0, -1):
        print(f'{line}*{col}={col*line}\t', end='')
    print()
