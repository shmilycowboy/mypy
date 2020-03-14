while True:
    order_ending=('st','nd','rd')+('th',)*17+('st','nd','rd')+('th',)*7+('st',)
    day=input("请输入日期：")
    print(day+order_ending[int(day)-1])
