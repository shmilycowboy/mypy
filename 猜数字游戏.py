while True:
    import random
    secret = random.randint(0, 10)
    guess = int(input('猜猜看我心里的数字(1~10):'))
    time = 1
    if guess == secret:
        print('-------------------')
        print('神预测，收下我的膝盖！')
        print('-------------------')
    else:
        while guess != secret and time <= 2:
            time += 1
            if guess > 10:
                guess = int(input('数字必须小于等于10，请重新输入:'))
            elif guess < 1:
                guess = int(input('数字必须大于等于0，请重新输入:'))
            elif guess < secret:
                guess = int(input('小了，再来一次:'))
            else:
                guess = int(input('大了，再来一次:'))
        if time > 2 and guess != secret:
            print(f'你已经猜错超过3次了,游戏结束(提示:我心里的数字是{secret})')
        elif time == 2:
            print('还不错，两次就猜对了！')
        else:
            print('-----------------')
            print('终于猜对了，哈哈!')
            print('-----------------')
