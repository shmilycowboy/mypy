a_list = [1, 2, 3, 4]
b_list = a_list*3
c_list = a_list+[5]
c_list.append(6)
d_list = c_list[:]
d_list.extend([7, 8, 9, 10])
e_list = d_list[:]
f_list = e_list.insert(0, 0)  # list.insert(index，obj)无返回值。
g_list = e_list.append(11)  # list.append(obj)无返回值。
k_list = e_list.append([12, 13])  # list.extend([obj1,obj2])无返回值
obj = e_list.pop()  # list.pop(obj)有返回值，返回list[-1]
# list.sort()\list.pop()\list.append()\list.extend()\list.insert()都会使list发生变化
print('a_list:', a_list)
print('b_list:', b_list)  # 且除了list.pop()外，其他均无返回值
print('c_list:', c_list)
print('d_list:', d_list)
print('e_list:', e_list)
print('f_list:', f_list)
print('g_list:', g_list)
print('k_list:', k_list)
print('obj:', obj)
