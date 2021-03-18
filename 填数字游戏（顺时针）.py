num = int(input('please input a number:'))
num_list = [[0]*num]*num
direction = 'Right'  # 初始默认向右开始填充
j, k = 0, 0
for i in range(1, num*num+1):
    num_list[j][k] = i
    if j+k == num-1 and k >= num/2:  # or:j<=num/2 or:k>=j 这三种方法都可以实现。
        direction = 'Down'
    elif j == k and k >= num/2:
        direction = 'Left'
    elif j+k == num-1 and k < num/2:  # or:j>num/2 or:k<j 这三种方法都可以实现。
        direction = 'Up'
    elif j-k == 1 and j < num/2:
        direction = 'Right'
    if direction == 'Right':
        k += 1
    elif direction == 'Down':
        j += 1
    elif direction == 'Left':
        k -= 1
    elif direction == 'Up':
        j -= 1
for i in range(num):
    for j in range(num):
        print('%02d' % num_list[i][j], end=' ')
    print()
