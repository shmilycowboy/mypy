import random
secret=random.randint(0,10)
temp = input("Guess the number(1~10):")
guess = int(temp)
time = 1
while guess != secret and time<=2:
    time+=1
    if guess < secret:
        temp = input("smaller,another chance:")
        guess = int(temp)
    else:
        temp = input("bigger,another chance:")
        guess = int(temp)              
if time>2 and guess !=secret:
    print("You have missed over 3 times,game over")
else:
    print("Awesome,you did a good job!")
