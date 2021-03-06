a_tuple=('student',)
list_1=[2,3,5]
list_1.insert(1,a_tuple)  
list_1.insert(1,tuple('student'))  
print(type(a_tuple))
print(tuple('student'))
print(list_1)