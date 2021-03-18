height = int(input('input the height:'))
if height % 2 == 0:
    print('input error!')
else:
    for i in range(height):
        for blank in range(1, height-i):
            print(' ', end='')
        for j in range(i*2+1):
            print('*', end='')
        print()
    print('-------------------------------------------------')
    for i in range(height):
        print(' '*(height-i-1), end='')
        print('*'*(i*2+1))
