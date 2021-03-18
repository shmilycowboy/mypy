height = int(input('input the height:'))
if height % 2 == 0:
    print('input error!')
else:
    h = int((height+1)/2)
    for i in range(h):
        print(' '*(h-i-1), end='')
        print('*'*(i*2+1))
    for j in range(h-1, 0, -1):
        print(' '*(h-j), end='')
        print('*'*(j*2-1))
