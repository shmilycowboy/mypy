s_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
i = 0
a_list = []
b_list = []
c_list = []
while i < len(s_list):
    if s_list[i] % 3 == 0:
        a_list.append(s_list[i])
        i += 1
    elif s_list[i] % 3 == 1:
        b_list.append(s_list[i])
        i += 1
    else:
        c_list.append(s_list[i])
        i += 1
print('bei 3 zheng chu:', a_list)
print('yushu wei 1:', b_list)
print('yushu wei 2:', c_list)
