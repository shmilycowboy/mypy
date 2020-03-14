while True:
    score=int(input('input ur score:'))
    if score>100:
        print('Be serious and try again!')
    elif score>=90:
        print('Congratuations!your grade is A!')
    elif score>=80:
        print('Good,your grade is B!')
    elif score>=70:
        print('Not too bad,your grade is C!')
    elif score>=0:
        print('Sorry to tell you that your grade is D!')
    else:
        print('PLEASE check the score you input and try again!!!')