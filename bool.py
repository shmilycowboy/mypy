x = True
y = False
print('\tx\t'+'y\t')
print('x\t'+str(x and x)+str('\t')+str(x and y))
print('y\t'+str(y and x)+str('\t')+str(y and y))
print('\tx\t'+'y\t')
print('x\t'+str(x or x)+str('\t')+str(x or y))
print('y\t'+str(y or x)+str('\t')+str(y or y))
