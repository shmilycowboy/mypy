num = int(input('请输入需要求的范围：'))
premier_list = list(range(2, num+1))
for i in list(range(2, num+1)):  # 若写成for i in premier_list:则会发生错误，试分析原因。
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            premier_list.remove(i)
            break
print(premier_list)
print(len(premier_list))
