month=int(input('qing shu ru yue fen:'))
def num(month):
    if month==1:
        return 1
    elif month==2:
        return 1
    else:
        return num(month-1)+num(month-2)
print('tu zi de shu liang shi:%d'%(num(month)))