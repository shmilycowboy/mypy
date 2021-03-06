sum=input('请输入人民币金额:')
zheng=list(str(int(sum)))     #获取输入数字的字符形成list
unit=['千','百','十','亿','千','百','十','万','千','百','十','元']
del unit[:-len(zheng)]    #截取列表使得单位与输入数字的位数相匹配
trad={'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
trad_sum=[]
for i in zheng:
    trad_sum.append(trad[i]) #输入字符转换为大写格式
print(trad_sum)
print(unit)
for i in range(len(trad_sum)):
    if trad_sum[i]=='零':
        if unit[i] in ['千','百']:
            result_str='零'
        elif unit[i]=='十':
            if trad_sum[i+1]=='零':
                result_str=''
            else:
                result_str='零'           
        else:
            result_str=unit[i]
    else:
        result_str=trad_sum[i]+unit[i]
    print(result_str,end='') 

