print('for循环：')
a_list = []
for num in range(100, 1000):
    a = num//100
    b = (num % 100)//10
    c = num % 10
    if num == a**3+b**3+c**3:
        a_list.append(num)
print(a_list)
print('-------------------------------------')
print('for表达式法：')  # 一行代码就搞定
print([x for x in range(100, 1000) if (x//100)
       ** 3+((x % 100)//10)**3+(x % 10)**3 == x])
