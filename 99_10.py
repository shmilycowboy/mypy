for col in range(9,0,-1):
    for black in range(9-col):
        print('\t',end='')
    for line in range(col,0,-1):
        print(f'{line}*{col}={col*line}\t',end='')
    print()