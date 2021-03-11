list = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1]
list_copy = []
for i in list:
    if i not in list_copy:
        list_copy.append(i)
print(list_copy)
print('------------------------------------')
list = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1]
a_set = set(list)
# a_list=list(a_set) #list()函数无法将set类型list化。
print(a_set)
# print(a_list)
