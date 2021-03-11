a_list = list(range(1, 5))
a_list.insert(2, tuple('crazy'))  # 字符串tuple()后，字符串各个字符会分开
print(a_list)
print('----------------------------------')
a_tuple = ('student',)
list_1 = [2, 3, 5]
list_1.insert(1, a_tuple)
list_1.insert(1, tuple('student'))
print(type(a_tuple))
print(tuple('student'))
print(list_1)
print('---------------------------------')
a_list = [1, 2, 3]
b_list = ['a', 'b', 'c']
c_list = [x for x in zip(a_list, b_list)]
d_list = a_list+b_list
print(c_list)
print(d_list)
a_list.extend(b_list)
print(a_list)
a_list.append(b_list)
print(a_list)
print('---------------------------------')
