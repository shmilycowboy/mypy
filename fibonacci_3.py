month = int(input('input month:'))
month1 = 1
month2 = 1
for i in range(1, month-1):
    month1, month2 = month2, month1+month2
print(1 if month <= 2 else month2)
