num = int(input('input a number:'))
array = [[0]*num]
for i in range(num-1):
    array.append([0]*num)  # array+=[[0]*num]
j, k, o = 0, 0, 0
for i in range(1, num*num+1):
    array[j][k] = i
    if j+k == num-1 and k >= num/2:  # k>=num/2 #k>=j
        o = 1
    elif j == k and k >= num/2:
        o = 2
    elif j+k == num-1 and k < num/2:
        o = 3
    elif j-k == 1 and j < num/2:
        o = 0
    if o == 0:
        k += 1
    elif o == 1:
        j += 1
    elif o == 2:
        k -= 1
    elif o == 3:
        j -= 1
for i in range(num):
    for j in range(num):
        print('%02d' % array[i][j], end=' ')
    print()
