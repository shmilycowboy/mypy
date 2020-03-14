s_line = input("plz enter a number:")
s_line = int(s_line)
m = 1
while m <= s_line:
    print(' '*int((s_line-m)/2)+'*'*m)
    m += 2
    n = m-2
while n >= 1:
    n -= 2
    print(' '*int((s_line-n)/2)+'*'*n)

