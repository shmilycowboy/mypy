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
