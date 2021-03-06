import random
secret = random.randint(0, 10)
guess = int(input('猜猜看我心里的数字(1~10):'))
time = 1
while guess != secret and time <= 2:
    time += 1
    if guess < secret:
        guess = int(input('小了，再来一次:'))
    else:
        guess = int(input('大了，再来一次:'))
if time > 2 and guess != secret:
    print(f'你已经猜错超过3次了,游戏结束(提示:我心里的数字是{secret})')
else:
    print('哈哈,你简直是我肚子里的蛔虫呀!')
