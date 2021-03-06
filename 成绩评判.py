while True:
    score=int(input('请输入成绩:'))
    if score>100:
        print('认真一点啊，拜托!')
    elif score>=90:
        print('恭喜你，你的成绩是A!')
    elif score>=80:
        print('不错，你的成绩是B!')
    elif score>=60:
        print('不算太坏，你的成绩是C!')
    elif score>=0:
        print('很遗憾，你的成绩是D!')
    else:
        print('请检查你输入的成绩是否有误!!!')