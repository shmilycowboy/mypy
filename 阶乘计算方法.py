num = int(input("请输入需要求阶乘的数字:"))
result = 1
for i in range(1, num+1):
    result *= i
print(f'常规法计算该数字的阶乘为:{result}')
print('-----------------------------------------')
def jc(x):
    if x==0 or x==1:
        return 1
    else:
        return x*jc(x-1)
print(f'递归法求得该数字的阶乘为：{jc(num)}')
