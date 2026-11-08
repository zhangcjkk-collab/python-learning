import random

num = random.randint(1,100)

a = int(input("请输入第一次猜想的数字："))
if a == num:
    print("恭喜你，答对了")
else:
    if a < num:
        b = int(input("不对，猜小了，再猜一次："))
    else:
        b = int(input("不对，猜大了，再猜一次："))
    if b == num:
        print("恭喜你，答对了")
    else:
        if b < num:
            c = int(input("不对，猜小了，再猜最后一次："))
        else:
            c = int(input("不对，猜大了，再猜最后一次："))
        if c == num:
             print("恭喜你，答对了")
        else:
            print(f"都答错了，我想的是{num}")