s_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
i = 0
a_list = []
b_list = []
c_list = []
while i < len(s_list):
    if s_list[i] % 3 == 0:
        a_list.append(s_list[i])
    elif s_list[i] % 3 == 1:
        b_list.append(s_list[i])
    else:
        c_list.append(s_list[i])
    i += 1
print('被3整除:', a_list)
print('余数为1:', b_list)
print('余数为2:', c_list)
