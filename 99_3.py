for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print(f'{j}*{i}={j*i}\t',end='')
    print()    