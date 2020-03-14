i,j=1,9
while j>=1:
    if i<j:
        print(f'{i}*{j}={i*j}\t',end='')
        i+=1
    elif i==j:
        print(f'{i}*{j}={i*j}\t')
        j-=1
        i=1