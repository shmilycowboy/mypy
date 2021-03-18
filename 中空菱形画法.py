height = int(input('input the height:'))
if height % 2 == 0:
    print('input error!')
else:
    h = int((height+1)/2)
    print(' '*(h-1)+'*')
    for i in range(1, h):
        print(' '*(h-i-1), end='')
        print('*'+' '*(i*2-1)+'*')
    for j in range(h-1, 1, -1):
        print(' '*(h-j), end='')
        print('*'+' '*(j*2-3)+'*')
    print(' '*(h-1)+'*')
