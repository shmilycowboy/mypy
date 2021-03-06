def jc(x):
    if x==0 or x==1:
        return 1
    else:
        return x*jc(x-1)
while True:
    num=int(input('input a number:'))
    print(jc(num))