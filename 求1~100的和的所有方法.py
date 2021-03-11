print('函数法：')
print(sum(range(1, 101)))
print('--------------------------------------------')
print('while循环：')
result, i = 1, 1
while i < 100:
    i += 1
    result += i
print(result)
print('--------------------------------------------')
print('for循环法：')
result = 0
for i in range(1, 101):
    result += i
print(result)
print('--------------------------------------------')
print('递归法：')


def result(i):
    if i == 1:
        return 1
    else:
        return result(i-1)+i


print(result(100))
print('--------------------------------------------')
