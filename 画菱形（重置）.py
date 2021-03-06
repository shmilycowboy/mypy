
def draw(height):
    for line in range(height):
        if line*2 < height:
            for blank in range(1, int((height+1)/2)-line):
                print(' ', end='')
            for star in range(line*2+1):
                print('*', end='')
        else:
            for blank in range(line+1-int((height+1)/2)):
                print(' ', end='')
            for star in range((height-line)*2-1):
                print('*', end='')
        print()



while True:
    height = int(input('input the height:'))
    if height % 2 == 0:
        print('input error')
    else:
        draw(height)