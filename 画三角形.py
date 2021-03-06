while True:
    height=int(input('input the height:'))
    for i in range(height):
        for blank in range(1,height-i):
            print(' ',end='')
        for j in range(i*2+1):
            print('*',end='')
        print()
