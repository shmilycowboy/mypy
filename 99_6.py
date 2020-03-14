for col in range(9,0,-1):
    for line in range(1,col+1):
        print(f'{line}*{col}={line*col}\t',end='')
    for black in range(9-col):
        print('\t',end='')
    print()