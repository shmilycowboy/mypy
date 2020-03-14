s_month=int(input('input month:'))
a_list=[1,1]
for month in range(s_month-2):
    a_list.append(a_list[-1]+a_list[-2])
print(a_list[-1])
