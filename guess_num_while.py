import random

num = random.randint(1,100)

count = 0
while count < 7:
    guess = int(input("猜猜我想的数："))
    count += 1
    if guess == num:
        print("恭喜你答对了！")
        break
    elif guess < num:
        print("抱歉，你猜小了")
    else:
        print("抱歉，你猜大了")
if guess == num:
    print(f"你用了{count}次猜到正确答案")
else:
    print("抱歉，你七次都没猜对")
